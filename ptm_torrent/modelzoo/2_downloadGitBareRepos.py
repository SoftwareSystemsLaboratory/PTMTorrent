from pathlib import PurePath
from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

from ptm_torrent.modelzoo import (expectedMZMetadataJSONFilePath,
                                  gitCloneBarePath)
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneBareRepo


def readJSONData(json: List[dict]) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data...") as spinner:
        obj: dict
        for obj in json:
            data.append(obj["link"])
            spinner.next()

    return data


def cloneGitBareRepos(urls: List[str], gitCloneBarePath: PurePath) -> None:
    url: str
    with Bar(f"Cloning git repos to {gitCloneBarePath}...", max=len(urls)) as bar:
        for url in urls:
            cloneBareRepo(url, gitCloneBarePath)
            bar.next()


def main() -> None | bool:
    if testForFile(path=expectedMZMetadataJSONFilePath) == False:
        return False

    jsonData: List[dict] = readJSON(jsonFilePath=expectedMZMetadataJSONFilePath)[
        "models"
    ]

    urls: List[str] = readJSONData(json=jsonData)

    cloneGitBareRepos(urls, gitCloneBarePath)


if __name__ == "__main__":
    main()
