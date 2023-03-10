from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

import ptm_torrent.onnxmodelzoo as omz
from ptm_torrent.utils.fileSystem import saveJSON, testForFile, testForPath
from ptm_torrent.utils.git import getLatestGitCommitOfFile
from ptm_torrent.utils.ptmSchema import ModelHub, PTMTorrent


def createModelHub(row: Series) -> ModelHub:
    mh: ModelHub = ModelHub(
        metadata_file_path=omz.onnxmodelzoo_HubJSONMetadataPath.__str__(),
        metadata_object_id=str(row["id"]),
        model_hub_name="Onnx Model Zoo",
        model_hub_url="https://github.com/onnx/models",
    )
    return mh


def createPTMSchema(df: DataFrame) -> List[dict]:
    data: List[dict] = []

    with Bar("Creating PTM Torrent objects...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):

            row: Series = df.loc[idx]

            url: str = row["GitHub URL"]
            parsedURL: ParseResult = urlparse(url)
            urlPath: str = str(parsedURL.path).strip("/")

            repoPath: PurePath = PurePath(f"{omz.onnxmodelzoo_GitRepoPath}")
            if testForPath(repoPath) == False:
                print(f"Path not found: {repoPath}")
                bar.next()
                continue

            splitPath: list = urlPath.split("/")

            ptm: PTMTorrent = PTMTorrent(
                id=idx,
                latest_git_commit_sha=getLatestGitCommitOfFile(
                    gitProjectPath=repoPath, filepath=row["ModelPath"]
                ),
                model_hub=createModelHub(row),
                model_name=row["Model"],
                model_owner="ONNX",
                model_owner_url="https://github.com/onnx",
                datasets=None,
                model_url=url,
                model_architecture=None,
                model_paper_dois=[],
                model_task=row["Category"],
            )

            data.append(ptm.to_dict())

            bar.next()

    return data


def main() -> None | bool:
    if testForFile(path=omz.onnxmodelzoo_ConcatinatedModelMetadataPath) == False:
        return False

    jsonFilePath: PurePath = PurePath(
        f"{omz.rootFolderPath}/{omz.jsonFolderPath}/onnxmodelzoo.json"
    )

    df: DataFrame = pandas.read_json(
        path_or_buf=omz.onnxmodelzoo_ConcatinatedModelMetadataPath
    )

    json: List[dict] = createPTMSchema(df)

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
