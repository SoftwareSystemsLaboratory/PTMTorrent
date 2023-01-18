from json import dump, load
from os import mkdir
from os.path import isdir, isfile
from pathlib import PurePath
from typing import List

from bs4 import BeautifulSoup


def createPath(path: PurePath) -> bool:
    try:
        mkdir(path)
    except FileExistsError:
        pass
    return isdir(path)


def saveJSON(json: List[dict], filepath: PurePath = "data.json") -> None:
    with open(filepath, "w") as jsonFile:
        dump(json, jsonFile, indent=4)
        jsonFile.close()


def saveHTML(html: str, filepath: PurePath = "data.html") -> None:
    soup: BeautifulSoup = BeautifulSoup(markup=html)
    prettyHTML: str = soup.prettify()

    with open(filepath, "w") as htmlFile:
        htmlFile.write(prettyHTML)
        htmlFile.close()


def readJSON(jsonFilePath: PurePath) -> dict:
    with open(jsonFilePath, "r") as jsonFile:
        jsonData: dict = load(jsonFile)
        jsonFile.close()

    return jsonData


def testForFile(path: PurePath) -> bool:
    return isfile(path)


def testForPath(path: PurePath) -> bool:
    return isdir(path)
