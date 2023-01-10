import re
from argparse import ArgumentParser, Namespace
from json import dumps
from pprint import pprint as print
from re import Match, Pattern
from time import time
from typing import List

import pandas
from huggingface_hub import list_models
from huggingface_hub.hf_api import ModelInfo
from pandas import DataFrame
from progress.bar import Bar


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


def matchInArray(regex: str, array: list) -> list:
    data: list = []
    pattern: Pattern = re.compile(regex)

    item: str
    for item in array:
        match: Match = pattern.match(item)
        if match:
            data.append(match.string)

    return data


def iterDF(df: DataFrame) -> dict:
    idx: int
    for idx in range(len(df)):
        dois: list = []
        idKey: int = df.loc[idx, "_id"]
        modelID: str = df.loc[idx, "modelId"]
        author: str | None = df.loc[idx, "author"]
        sha: str = df.loc[idx, "sha"]

        try:
            modelName: str = modelID.split("/")[1]
        except IndexError:
            modelName: str = modelID

        stor: dict = {
            "id": idKey,
            "ModelHub": {
                "ModelHubName": "Hugging Face",
                "MetadataFilePath": filepath,
                "MetadataObjectID": idKey,
            },
            "ModelName": modelName,
            "ModelOwner": author,
            "ModelURL": f"https://huggingface.co/{modelID}",
            "ModelOwnerURL": f"https://huggingface.co/{author}",
            "Datasets": [{}],
            "ModelPaperDOI": dois,
            "LatestGitCommitSHA": sha,
        }

        modelTags: list = df.loc[idx, "tags"]

        tag: str
        for tag in modelTags:
            match: Match = doiPattern.match(tag)
            if match:
                stor["ModelPaperDOI"].append(match.string)

        try:
            stor["ModelTask"] = df.loc[idx, "pipeline_tag"]
        except TypeError:
            stor["ModelTask"] = None
        except KeyError:
            stor["ModelTask"] = None

        try:
            stor["ModelArchitecture"] = df.loc[idx, "config"]["model_type"]
        except TypeError:
            stor["ModelArchitecture"] = None
        except KeyError:
            stor["ModelArchitecture"] = None


def main() -> None:
    args: Namespace = getArgs()

    timestamp: int | str
    if args.timestamp is None:
        timestamp = int(time())
    else:
        timestamp = args.timestamp

    modelList: list = getModelList()

    df: DataFrame = pandas.read_json(dumps(modelList))


doiRegex: str = "^.*(arxiv|doi).*$"
datasetRegex: str = "^.*(dataset).*$"

doiPattern: Pattern = re.compile(pattern=doiRegex)
datasetPattern: Pattern = re.compile(pattern=datasetRegex)

# filepath: str = f"./data/json/models_{timestamp}.json"


# df.to_json(filepath)

if __name__ == "__main__":
    main()
