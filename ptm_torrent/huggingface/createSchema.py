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

            # Pull current entry from table
            row: Series = df.loc[idx]

            # Find model owner information
            model_owner:str
            model_owner_url: str

            # Check if owner info is populated
            if row["author"] == None:
                model_owner = "http://huggingface.co/"
                model_owner_url = "http://huggingface.co/"
            else:
                model_owner = str(row["author"])
                model_owner_url = f'https://huggingface.co/{model_owner}'


            # Find architecture
            model_architecture: str = None
            # Check if config>model_type exists
            config = row["config"]
            if config != None:
                if "model_type" in config:
                    model_architecture = config["model_type"]

            # Find task
            model_task = row["pipeline_tag"]

            # Get dois
            model_paper_dois: List[str] = None               
            tags: List[str] = row["tags"]
            if tags != None:
                temp = [x for x in tags if "doi:" in x]
                if temp:
                    model_paper_dois = temp
            

            ptm: PTMTorrent = PTMTorrent(
                id=idx,
                latest_git_commit_sha=row["sha"],
                model_hub=createModelHub(row),
                model_name=str(row["id"]),
                model_owner=model_owner,
                model_owner_url=model_owner_url,
                model_url=f'https://huggingface.co/{row["id"]}',
                datasets= None,# TODO
                model_architecture= model_architecture,
                model_paper_dois= model_paper_dois,# TODO
                model_task= model_task,
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
