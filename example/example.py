import json
import re
from json import load
from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse


def readJSON(filepath: PurePath) -> List[dict]:
    with open(filepath, "r") as jsonFile:
        data: List[dict] = load(jsonFile)
        jsonFile.close()
    return data


def extractAuthorRepo(url: str) -> PurePath:
    parsedURL: ParseResult = urlparse(url)
    path: str = parsedURL.path.strip()

    splitPath: List[str] = path.strip("/").split("/")

    author: str
    repo: str
    try:
        author = splitPath[0]
        repo = splitPath[1]
    except IndexError:
        author = parsedURL.netloc
        repo = splitPath[0]

    return PurePath(f"{author}/{repo}")


def main():
    paths: List[PurePath] = []

    jsonFile: PurePath = PurePath("onnxmodelzoo.json")
    json: List[dict] = readJSON(filepath=jsonFile)

    data: dict
    for data in json:
        modelURL: str = data["ModelURL"]
        authorRepo: PurePath = extractAuthorRepo(url=modelURL)
        paths.append(authorRepo)

    paths: set[PurePath] = set(paths)

    path: PurePath
    for path in paths:
        print(path.__str__())


if __name__ == "__main__":
    main()
