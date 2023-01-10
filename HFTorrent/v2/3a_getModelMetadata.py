import re
from argparse import ArgumentParser, Namespace
from json import dumps
from pathlib import PurePath
from re import Match, Pattern
from time import time
from typing import List
from warnings import filterwarnings

import pandas
from huggingface_hub import list_models
from huggingface_hub.hf_api import ModelInfo
from mhObject import ModelHub
from pandas import DataFrame, Series
from progress.bar import Bar
from schemaObject import Schema

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


def matchInArray(regex: str, array: list) -> list:
    data: list = []
    pattern: Pattern = re.compile(regex)

    item: str
    for item in array:
        match: Match = pattern.match(item)
        if match:
            data.append(match.string)

    return data


def testTag(test) -> str | None:
    try:
        return test
    except TypeError:
        return None
    except KeyError:
        return None


def buildModelHubObject(metadataFilePath: PurePath, id: int) -> ModelHub:
    obj: ModelHub = ModelHub()

    obj.setModelHubName("Hugging Face")
    obj.setMetadataFilePath(metadataFilePath)
    obj.setMetadataObjectID(id)

    return obj


def buildSchemaObject(series: Series, metadataFilePath: PurePath) -> Schema:
    obj: Schema = Schema()

    id: int = series["_id"]
    modelID: str = series["modelId"]
    tags: list = series["tags"]

    obj.setID(id)
    obj.setModelHub(buildModelHubObject(metadataFilePath, id))
    obj.setModelOwner(series["author"])
    obj.setModelURL(f"https://huggingface.co/{modelID}")
    obj.setModelOwnerURL(f'https://huggingface.co/{series["author"]}')
    obj.setDatasets([])
    obj.setLatestGitCommitSHA(series["sha"])
    obj.setModelTasks(testTag(series["pipeline_tag"]))

    try:
        obj.setModelArchitecture(testTag(series["config"])["model_type"])
    except TypeError:
        obj.setModelArchitecture(None)
    except KeyError:
        obj.setModelArchitecture(None)

    try:
        obj.setModelName(modelID.split("/")[1])
    except IndexError:
        obj.setModelName(modelID)

    obj.setModelPaperDOIs(matchInArray(regex=doiRegex, array=tags))

    return obj


def main() -> None:
    args: Namespace = getArgs()

    timestamp: int | str
    if args.timestamp is None:
        timestamp = int(time())
    else:
        timestamp = args.timestamp

    filepath: PurePath = PurePath(f"./data/json/models_{timestamp}.json")

    modelList: list = getModelList()

    df: DataFrame = pandas.read_json(dumps(modelList))

    with Bar("Creating data schema...", max=len(df)) as bar:
        idx: int
        for idx in range(len(df)):
            series: Series = df.loc[idx]
            buildSchemaObject(series, metadataFilePath=filepath)
            bar.next()


# df.to_json(filepath)

if __name__ == "__main__":
    main()
