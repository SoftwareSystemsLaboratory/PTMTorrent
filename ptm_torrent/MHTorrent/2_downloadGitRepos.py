from concurrent.futures import ThreadPoolExecutor
from json import load
from os.path import isfile
from pathlib import PurePath
from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

from ptm_torrent.utils.git import cloneRepo


def testForFile(path: PurePath) -> bool:
    if isfile(path) == False:
        print("ModelHub metadata not in the expected location")
        return False
    return True


def readJSONData(json: dict) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data for GitHub URLs...") as spinner:
        obj: dict
        for obj in json:
            data.append(obj["github"])
            spinner.next()

    return data


def cloneGitRepos(urls: List[str], rootGitClonePath: PurePath) -> None:
    url: str
    with Bar(f"Cloning git repos to {rootGitClonePath}...", max=len(urls)) as bar:
        for url in urls:
            cloneRepo(url, rootGitClonePath)
            bar.next()


def main() -> None | bool:
    rootGitClonePath: PurePath = PurePath("repos")
    expectedMHMetadataJSONFilePath: PurePath = PurePath(
        "json/metadata/mh_metadata.json"
    )

    if testForFile(path=expectedMHMetadataJSONFilePath) == False:
        return False

    with open(expectedMHMetadataJSONFilePath, "r") as jsonFile:
        jsonData: dict = load(jsonFile)
        jsonFile.close()

    urls: List[str] = readJSONData(json=jsonData)

    cloneGitRepos(urls, rootGitClonePath)


if __name__ == "__main__":
    main()
