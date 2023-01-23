from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

import ptm_torrent.modelhub as mh
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


def main() -> None | bool:
    if testForFile(path=mh.modelhub_HubMetadataPath) == False:
        return False

    jsonData: dict = readJSON(jsonFilePath=mh.modelhub_HubMetadataPath)

    urls: List[str] = readJSONData(json=jsonData)

    with Bar(f"Cloning git repos to {mh.reposFolderPath}...", max=len(urls)) as bar:
        url: str
        for url in urls:
            cloneRepo(url=url, rootGitClonePath=mh.modelhub_ReposPath)
            bar.next()


if __name__ == "__main__":
    main()
