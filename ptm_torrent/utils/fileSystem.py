from json import dump
from os import mkdir
from os.path import isdir
from pathlib import PurePath


def createPath(path: PurePath) -> bool:
    try:
        mkdir(path=path)
    except FileExistsError:
        pass
    return isdir(s=path)


def saveJSON(json: dict, filepath: PurePath = "data.json") -> bool:
    with open(filepath, "w") as jsonFile:
        dump(json, jsonFile, indent=4)
        jsonFile.close()
