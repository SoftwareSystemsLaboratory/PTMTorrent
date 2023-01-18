from json import dump, load
from os import mkdir
from os.path import isdir, isfile
from pathlib import PurePath
from typing import List

from progress.spinner import Spinner


def createPath(path: PurePath) -> bool:
    try:
        mkdir(path)
    except FileExistsError:
        pass
    return isdir(path)


def saveJSON(json: List[dict], filepath: PurePath = "data.json") -> bool:
    with open(filepath, "w") as jsonFile:
        dump(json, jsonFile, indent=4)
        jsonFile.close()


def readJSON(jsonFilePath: PurePath) -> dict:
    with open(jsonFilePath, "r") as jsonFile:
        jsonData: dict = load(jsonFile)
        jsonFile.close()

    return jsonData


def testForFile(path: PurePath) -> bool:
    return isfile(path)


def testForPath(path: PurePath) -> bool:
    return isdir(path)
