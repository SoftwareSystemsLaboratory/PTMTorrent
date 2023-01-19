from concurrent.futures import ThreadPoolExecutor
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
    with ThreadPoolExecutor() as executor:
        with Bar(f"Cloning git repos to {rootGitClonePath}...", max=len(urls)) as bar:

            def _concurrurentHelper(url: str) -> None:
                cloneRepo(url, rootGitClonePath)
                bar.next()

            results = executor.map(_concurrurentHelper, urls)


def main() -> None | bool:
    if testForFile(path=expectedMHMetadataJSONFilePath) == False:
        return False

    jsonData: dict = readJSON(jsonFilePath=expectedMHMetadataJSONFilePath)

    urls: List[str] = readJSONData(json=jsonData)

    cloneGitRepos(urls, rootGitClonePath)


if __name__ == "__main__":
    main()
