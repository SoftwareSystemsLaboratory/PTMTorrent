from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import saveJSON, testForFile, testForPath
from ptm_torrent.utils.git import getLatestGitCommitOfFile
from ptm_torrent.utils.ptmSchema import ModelHub, PTMTorrent


def createModelHub(row: Series) -> ModelHub:
    mh: ModelHub = ModelHub(
        metadata_file_path=hf.huggingface_HubMetadataPath.__str__(),
        metadata_object_id=str(row["id"]),
        model_hub_name="Hugging Face",
        model_hub_url="https://huggingface.co/",
    )
    return mh


def createPTMSchema(df: DataFrame) -> List[dict]:
    data: List[dict] = []

    with Bar("Creating PTM Torrent objects...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):

            row: Series = df.loc[idx]

            # url: str = row["GitHub URL"]
            # parsedURL: ParseResult = urlparse(url)
            # urlPath: str = str(parsedURL.path).strip("/")

            # repoPath: PurePath = PurePath(f"{hf.huggingface_GitRepoPath}")
            # if testForPath(repoPath) == False:
            #     print(f"Path not found: {repoPath}")
            #     bar.next()
            #     continue

            # splitPath: list = urlPath.split("/")

            ptm: PTMTorrent = PTMTorrent(
                id=idx,
                latest_git_commit_sha=row["sha"],
                model_hub=createModelHub(row),
                model_name=str(row["modelId"]),
                model_owner=str(row["author"]),
                model_owner_url="", # TODO
                datasets=None,# TODO
                model_url="", # TODO
                model_architecture="", # TODO
                model_paper_dois=None,# TODO
                model_task=None,# TODO
            )

            data.append(ptm.to_dict())

            bar.next()

    return data


def main() -> None | bool:
    if testForFile(path=hf.huggingface_HubMetadataPath) == False:
        return False

    jsonFilePath: PurePath = PurePath(
        f"{hf.rootFolderPath}/{hf.jsonFolderPath}/huggingface.json"
    )

    df: DataFrame = pandas.read_json(
        path_or_buf=hf.huggingface_HubMetadataPath
    )

    json: List[dict] = createPTMSchema(df)

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
