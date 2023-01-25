from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

import ptm_torrent.pytorchhub as pyth
from ptm_torrent.utils.fileSystem import saveJSON, testForFile, testForPath
from ptm_torrent.utils.git import getLatestGitCommit
from ptm_torrent.utils.ptmSchema import ModelHub, PTMTorrent


def createModelHub(row: Series) -> ModelHub:
    mh: ModelHub = ModelHub(
        metadata_file_path=pyth.pytorchhub_ConcatinatedModelMetadataPath.__str__(),
        metadata_object_id=str(row["id"]),
        model_hub_name="PyTorch Hub",
        model_hub_url="https://pytorch.com/hub",
    )
    return mh


def createPTMSchema(df: DataFrame) -> List[dict]:
    data: List[dict] = []

    with Bar("Creating PTM Torrent objects...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):

            row: Series = df.loc[idx]

            url: str = row["GitHubURL"]
            parsedURL: ParseResult = urlparse(url)
            urlPath: str = str(parsedURL.path).strip("/")

            repoPath: PurePath = PurePath(f"{pyth.pytorchhub_ReposPath}")
            if testForPath(repoPath) == False:
                print(f"Path not found: {repoPath}")
                bar.next()
                continue

            splitPath: list = urlPath.split("/")

            ptm: PTMTorrent = PTMTorrent(
                id=idx,
                latest_git_commit_sha=getLatestGitCommit(gitProjectPath=repoPath),
                model_hub=createModelHub(row),
                model_name=row["ModelName"],
                model_owner=row["ModelAuthor"],
                model_owner_url="/".join(url.split("/")[0:-1]),
                datasets=None,
                model_url=url,
                model_architecture=None,
                model_paper_dois=[],
                model_task=None,
            )

            data.append(ptm.to_dict())

            bar.next()

    return data


def main() -> None | bool:
    if testForFile(path=pyth.pytorchhub_ConcatinatedModelMetadataPath) == False:
        return False

    jsonFilePath: PurePath = PurePath(
        f"{pyth.rootFolderPath}/{pyth.jsonFolderPath}/pytorchhub.json"
    )

    df: DataFrame = pandas.read_json(
        path_or_buf=pyth.pytorchhub_ConcatinatedModelMetadataPath
    )

    json: List[dict] = createPTMSchema(df)

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
