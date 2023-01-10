from argparse import ArgumentParser, Namespace
from json import dumps
from pathlib import PurePath
from time import time
from typing import List
from warnings import filterwarnings

import pandas
from huggingface_hub.hf_api import DatasetInfo, list_datasets
from pandas import DataFrame
from progress.bar import Bar

# Hides huggingface_hub list_model warning
filterwarnings(action="ignore")


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Hugging Face dataset metadata downloader"
    )
    parser.add_argument(
        "-t",
        "--timestamp",
        required=False,
        help="Timestamp to append to the end of the output file",
    )
    return parser.parse_args()


def getDatasetList() -> list:
    datasetList: list = []

    print("Getting all datasets hosted on Hugging Face...")
    resp: List[DatasetInfo] = list_datasets(full=True)

    with Bar("Converting response to JSON...", max=len(resp)) as bar:
        dataset: DatasetInfo
        for dataset in list(iter(resp)):
            datasetDict: dict = dataset.__dict__
            datasetList.append(datasetDict)
            bar.next()

    return datasetList


def main() -> None:
    args: Namespace = getArgs()

    timestamp: int | str
    if args.timestamp is None:
        timestamp = int(time())
    else:
        timestamp = args.timestamp

    filepath: PurePath = PurePath(f"./data/json/datasets_{timestamp}.json")

    datasetList: list = getDatasetList()

    df: DataFrame = pandas.read_json(dumps(datasetList))


if __name__ == "__main__":
    main()
