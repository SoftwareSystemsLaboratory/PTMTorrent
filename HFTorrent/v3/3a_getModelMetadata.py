from argparse import ArgumentParser, Namespace
from json import dump, dumps
from time import time
from typing import List
from warnings import filterwarnings

import pandas
from huggingface_hub.hf_api import ModelInfo, list_models
from pandas import DataFrame
from progress.bar import Bar
from ptmSchema import ModelHub, PTMTorrent

# Hides huggingface_hub list_model warning
filterwarnings(action="ignore")


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Hugging Face model metadata downloader"
    )
    parser.add_argument(
        "-t",
        "--timestamp",
        required=False,
        help="Timestamp to append to the end of the output file",
    )
    return parser.parse_args()


def getModelList() -> list:
    modelList: list = []

    print("Getting all PTMs hosted on Hugging Face...")
    resp: List[ModelInfo] = list_models(full=True, cardData=True, fetch_config=True)

    with Bar("Converting response to JSON...", max=len(resp)) as bar:
        model: ModelInfo
        for model in list(iter(resp)):
            modelDict: dict = model.__dict__
            modelDict["siblings"] = [file.__dict__ for file in modelDict["siblings"]]
            modelList.append(modelDict)
            bar.next()
    return modelList


def extractToSchema(df: DataFrame, metadataFilepath: str) -> List[dict]:
    data: List[dict] = []

    with Bar("Extracting data into JSON Schema compatible JSON...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):
            authorName: str = df.loc[idx, "modelId"].split("/")
            try:
                author: str = authorName[0]
                name: str = authorName[1]
            except IndexError:
                author: str = "Hugging Face implementation"
                name: str = authorName[0]

            id: int = idx
            mh: ModelHub = ModelHub(
                metadata_file_path=metadataFilepath,
                metadata_object_id=df.loc[idx, "_id"],
                model_hub_name="Hugging Face",
                model_hub_url="https://huggingface.co",
            )
            ModelName: str = name
            ModelOwner: str = author
            ModelURL: str = f"https://huggingface.co/{authorName}"
            ModelOwnerURL: str = f"https://huggingface.co/{author}"
            Datasets = None
            ModelPaperDOI: str = ""
            LatestGitCommitSHA: str = df.loc[idx, "sha"]
            ModelTask: str = df.loc[idx, "pipeline_tag"]
            ModelArchitecture: str = ""

            ptm: PTMTorrent = PTMTorrent(
                datasets=Datasets,
                id=id,
                latest_git_commit_sha=LatestGitCommitSHA,
                model_architecture=ModelArchitecture,
                model_hub=mh,
                model_name=ModelName,
                model_owner=ModelOwner,
                model_owner_url=ModelOwnerURL,
                model_paper_doi=ModelPaperDOI,
                model_task=ModelTask,
                model_url=ModelURL,
            )

            data.append(ptm.to_dict())
            bar.next()

    return data


def main() -> None:
    args: Namespace = getArgs()

    timestamp: int | str
    if args.timestamp is None:
        timestamp = int(time())
    else:
        timestamp = args.timestamp

    metadataFilepath: str = f"./huggingface_metadata_{timestamp}.json"
    ptmTorrentFilepath: str = f"huggingface_ptmtorrent_{timestamp}.json"

    modelsJSON: list = getModelList()

    print("Inserting JSON into DataFrame...")
    modelsDF: DataFrame = pandas.read_json(dumps(modelsJSON))

    print(f"Saving Hugging Face metadata data to {metadataFilepath}")
    modelsDF.to_json(path_or_buf=metadataFilepath, indent=4)

    ptms: List[dict] = extractToSchema(df=modelsDF, metadataFilepath=metadataFilepath)

    print(f"Saving Hugging Face PTMTorrent data to {ptmTorrentFilepath}")
    with open(ptmTorrentFilepath, "w") as fp:
        dump(ptms, fp)
        fp.close()


if __name__ == "__main__":
    main()
