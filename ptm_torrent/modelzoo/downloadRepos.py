from pathlib import PurePath
from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

import ptm_torrent.modelzoo as mz
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneRepo


def readJSONData(json: List[dict]) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data...") as spinner:
        obj: dict
        for obj in json:
            data.append(obj["link"])
            spinner.next()

    return data


def cloneGitRepos(urls: List[str], gitCloneBarePath: PurePath) -> None:
    url: str
    with Bar(f"Cloning git repos to {gitCloneBarePath}...", max=len(urls)) as bar:
        for url in urls:
            cloneRepo(url, gitCloneBarePath)
            bar.next()


def main() -> None | bool:
    if testForFile(path=mz.modelzoo_ConcatinatedModelMetadataPath) == False:
        return False

    jsonData: List[dict] = readJSON(
        jsonFilePath=mz.modelzoo_ConcatinatedModelMetadataPath
    )

    urls: List[str] = readJSONData(json=jsonData)

    cloneGitRepos(urls=urls, gitCloneBarePath=mz.modelzoo_ReposPath)


if __name__ == "__main__":
    main()
