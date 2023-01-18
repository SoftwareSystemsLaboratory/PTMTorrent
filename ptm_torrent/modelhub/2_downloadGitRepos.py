from pathlib import PurePath
from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

from ptm_torrent.modelhub import (expectedMHMetadataJSONFilePath,
                                   rootGitClonePath)
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneRepo


def readJSONData(json: dict) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data...") as spinner:
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
    if testForFile(path=expectedMHMetadataJSONFilePath) == False:
        return False

    jsonData: dict = readJSON(jsonFilePath=expectedMHMetadataJSONFilePath)

    urls: List[str] = readJSONData(json=jsonData)

    cloneGitRepos(urls, rootGitClonePath)


if __name__ == "__main__":
    main()
