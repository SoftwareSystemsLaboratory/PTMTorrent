import re
from argparse import ArgumentParser, Namespace
from json import dump, dumps
from pathlib import PurePath
from re import Match, Pattern
from time import time
from typing import Any, List
from warnings import filterwarnings

import pandas
from huggingface_hub.hf_api import ModelInfo, list_models
from pandas import DataFrame, Series
from progress.bar import Bar
from ptmSchema import ModelHub, PTMTorrent

# Hides huggingface_hub list_model warning
filterwarnings(action="ignore")

doiRegex: str = "^.*(arxiv|doi).*$"
datasetRegex: str = "^.*(dataset).*$"


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


# def getDatasetList() -> list:
#     datasetList: list = []

#     print("Getting all datasets hosted on Hugging Face...")
#     resp: List[DatasetInfo] = list_datasets(full=True, cardData=True)

#     with Bar("Converting response to JSON...", max=len(resp)) as bar:
#         dataset: DatasetInfo
#         for dataset in list(iter(resp)):
#             datasetDict: dict = dataset.__dict__
#             datasetList.append(datasetDict)
#             bar.next()
#     return datasetList


def matchInArray(regex: str, array: list) -> list:
    data: list = []
    pattern: Pattern = re.compile(regex)

    item: str
    for item in array:
        match: Match = pattern.match(item)
        if match:
            data.append(match.string)

    return data


def extractToSchema(df: DataFrame, metadataFilepath: PurePath) -> List[dict]:
    modelArchitecture: str
    author: str
    name: str

    data: List[dict] = []

    with Bar("Extracting data into JSON Schema compatible JSON...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):
            dataSeries: Series = df.loc[idx]
            authorName: str = dataSeries["modelId"].split("/")

            try:
                author = authorName[0]
                name = authorName[1]
            except IndexError:
                author = "Hugging Face implementation"
                name = authorName[0]

            try:
                modelArchitecture = dataSeries["config"]["model_type"]
            except TypeError:
                modelArchitecture = ""
            except KeyError:
                modelArchitecture = ""

            tags: list = dataSeries["tags"]

            id: int = idx
            mh: ModelHub = ModelHub(
                metadata_file_path=metadataFilepath.__str__(),
                metadata_object_id=dataSeries["_id"],
                model_hub_name="Hugging Face",
                model_hub_url="https://huggingface.co",
            )
            ModelName: str = name
            ModelOwner: str = author
            ModelURL: str = f"https://huggingface.co/{authorName}"
            ModelOwnerURL: str = f"https://huggingface.co/{author}"
            Datasets = None
            ModelPaperDOIs: List[Any] = matchInArray(regex=doiRegex, array=tags)
            LatestGitCommitSHA: str = dataSeries["sha"]
            ModelTask: str = dataSeries["pipeline_tag"]
            ModelArchitecture: str = modelArchitecture

            ptm: PTMTorrent = PTMTorrent(
                datasets=Datasets,
                id=id,
                latest_git_commit_sha=LatestGitCommitSHA,
                model_architecture=ModelArchitecture,
                model_hub=mh,
                model_name=ModelName,
                model_owner=ModelOwner,
                model_owner_url=ModelOwnerURL,
                model_paper_dois=ModelPaperDOIs,
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

    metadataFilepath: PurePath = PurePath(f"./huggingface_metadata_{timestamp}.json")
    ptmTorrentFilepath: PurePath = PurePath(f"huggingface_ptmtorrent_{timestamp}.json")

    modelsJSON: list = getModelList()

    print("Inserting JSON into DataFrame...")
    modelsDF: DataFrame = pandas.read_json(dumps(modelsJSON))

    ptms: List[dict] = extractToSchema(df=modelsDF, metadataFilepath=metadataFilepath)

    print(f"Saving Hugging Face PTMTorrent data to {ptmTorrentFilepath}")
    with open(ptmTorrentFilepath, "w") as fp:
        dump(ptms, fp)
        fp.close()

    print(f"Saving Hugging Face metadata data to {metadataFilepath}")
    modelsDF.T.to_json(path_or_buf=metadataFilepath, indent=4)


if __name__ == "__main__":
    main()
