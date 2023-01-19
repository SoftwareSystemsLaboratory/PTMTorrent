from glob import glob
from json import dump, load
from os import mkdir
from os.path import isdir, isfile
from pathlib import PurePath
from typing import List

from bs4 import BeautifulSoup
from markdown import markdown


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


def findFiles(globStr: str) -> List[PurePath]:
    """
    For specific file, use an exact filename.

    For all files that share a name, `filename` = '**/{NAME}'
    """
    filepaths: list[str] = glob(globStr, recursive=True)
    return [PurePath(path) for path in filepaths]


def markdownToHTML(outputDirectory: str, markdownFilepath: PurePath) -> PurePath:
    htmlFilepath: PurePath = PurePath(
        f"{outputDirectory}/{markdownFilepath.stem}_{markdownFilepath.parent.stem}.html"
    )

    with open(markdownFilepath, "r") as markdownFile:
        html: str = markdown(
            markdownFile.read(),
            extensions=["tables"],
            output_format="html",
            tab_length=4,
        )
        markdownFile.close()

    with open(htmlFilepath, "w") as htmlFile:
        htmlFile.write(html)
        htmlFile.close

    return htmlFilepath
