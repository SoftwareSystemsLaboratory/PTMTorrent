from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

import ptm_torrent.modelhub as mh
from ptm_torrent.utils.fileSystem import saveJSON, testForFile, testForPath
from ptm_torrent.utils.git import getLatestGitCommit
from ptm_torrent.utils.ptmSchema import ModelHub, PTMTorrent


def createModelHub(row: Series) -> ModelHub:
    mh: ModelHub = ModelHub(
        metadata_file_path=mh.modelhub_HubMetadataPath,
        metadata_object_id=row["id"],
        model_hub_name="Modelhub.ai",
        model_hub_url="https://modelhub.ai",
    )
    return mh


def createPTMSchema(df: DataFrame) -> List[dict]:
    data: List[dict] = []

    with Bar("Creating PTM Torrent objects...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):

            row: Series = df.loc[idx]

            url: str = row["github"]
            parsedURL: ParseResult = urlparse(url)
            urlPath: str = parsedURL.path.strip("/")

            repoPath: PurePath = PurePath(f"{mh.reposFolderPath}/{urlPath}")
            if testForPath(repoPath) == False:
                print(f"Path not found: {repoPath}")
                bar.next()
                continue

            splitPath: list = urlPath.split("/")

            ptm: PTMTorrent = PTMTorrent(
                id=idx,
                latest_git_commit_sha=getLatestGitCommit(gitProjectPath=repoPath),
                model_hub=createModelHub(row),
                model_name=row["name"],
                model_owner=splitPath[0],
                model_owner_url="/".join(url.split("/")[0:-1]),
                datasets=None,
                model_url=url,
                model_architecture=None,
                model_paper_dois=[],
                model_task=row["task_extended"],
            )

            data.append(ptm.to_dict())

            bar.next()

    return data


def main() -> None | bool:
    if testForFile(path=mh.modelhub_HubMetadataPath) == False:
        return False

    jsonFilePath: PurePath = PurePath(f"{mh.jsonFolderPath}/modelhub.ai.json")

    df: DataFrame = pandas.read_json(path_or_buf=mh.modelhub_HubMetadataPath)

    json: List[dict] = createPTMSchema(df)

    if testForPath(path=mh.jsonFolderPath) == False:
        return False

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
