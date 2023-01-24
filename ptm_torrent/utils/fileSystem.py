from glob import glob
from json import dump, load
from os import makedirs
from os.path import isdir, isfile
from pathlib import PurePath
from typing import List

from bs4 import BeautifulSoup
from markdown import markdown


def createPath(path: PurePath) -> bool:
    try:
        makedirs(path, exist_ok=False)
    except FileExistsError:
        print(f"Skipping {path.__str__()} as it already exists.")
    return isdir(path)


def saveJSON(json: List[dict], filepath: PurePath = "data.json") -> None:
    with open(filepath, "w") as jsonFile:
        dump(obj=json, fp=jsonFile, indent=4)
        jsonFile.close()


def saveHTML(html: str, filepath: PurePath = "data.html") -> None:
    soup: BeautifulSoup = BeautifulSoup(markup=html, features="lxml")
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
        )
        markdownFile.close()

    soup: BeautifulSoup = BeautifulSoup(markup=html, features="lxml")

    with open(htmlFilepath, "w") as htmlFile:
        htmlFile.write(soup.prettify())
        htmlFile.close

    return htmlFilepath


def readHTML(htmlFilePath: PurePath) -> BeautifulSoup:
    with open(htmlFilePath, "r") as htmlFile:
        soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")
        htmlFile.close()
    return soup


def setupFileSystem(
    rootFolderPath: PurePath, subfolderPaths: List[PurePath] = []
) -> None:

    paths: List[PurePath] = [rootFolderPath]
    rootPath: PurePath = paths[0]

    paths.extend([PurePath(f"{rootPath}/{subfolder}") for subfolder in subfolderPaths])

    path: PurePath
    for path in paths:
        print(f"Creating {path.__str__()}...")
        createPath(path)


def checkFileSystem(
    rootFolderPath: PurePath, subfolderPaths: List[PurePath] = []
) -> bool:
    """Returns True if all subfolders exist within the root folder"""
    paths: List[PurePath] = [rootFolderPath]
    rootPath: PurePath = paths[0]

    paths.extend([PurePath(f"{rootPath}/{subfolder}") for subfolder in subfolderPaths])

    path: PurePath
    for path in paths:
        if testForPath(path):
            continue
        else:
            return False
    return True
