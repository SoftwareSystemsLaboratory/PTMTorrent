from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

from ptm_torrent.modelhub import (expectedMHMetadataJSONFilePath,
                                  rootGitClonePath, rootJSONPath)
from ptm_torrent.utils.fileSystem import saveJSON, testForFile, testForPath
from ptm_torrent.utils.git import getLatestGitCommit
from ptm_torrent.utils.ptmSchema import ModelHub, PTMTorrent


def createModelHub(row: Series) -> ModelHub:
    mh: ModelHub = ModelHub(
        metadata_file_path=expectedMHMetadataJSONFilePath.__str__(),
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

            repoPath: PurePath = PurePath(f"{rootGitClonePath}/{urlPath}")
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
    if testForFile(path=expectedMHMetadataJSONFilePath) == False:
        return False

    jsonFilePath: PurePath = PurePath(f"{rootJSONPath}/modelhub.ai.json")

    df: DataFrame = pandas.read_json(path_or_buf=expectedMHMetadataJSONFilePath)

    json: List[dict] = createPTMSchema(df)

    if testForPath(path=rootJSONPath) == False:
        return False

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
