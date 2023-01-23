from typing import List

from progress.bar import Bar
from progress.spinner import Spinner

import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneRepo


def readJSONData(json: dict) -> List[str]:
    data: List[str] = []

    with Spinner("Reading JSON data...") as spinner:
        obj: dict
        for obj in json:
            data.append(f"https://huggingface.co/{obj['id']}")
            spinner.next()

    return data


def main() -> None | bool:
    if testForFile(path=hf.huggingface_HubMetadataPath) == False:
        return False

    jsonData: dict = readJSON(jsonFilePath=hf.huggingface_HubMetadataPath)

    urls: List[str] = readJSONData(json=jsonData)

    with Bar(
        f"Cloning git repos to {hf.huggingface_ReposPath}...", max=len(urls)
    ) as bar:
        url: str
        for url in urls:
            cloneRepo(url=url, rootGitClonePath=hf.huggingface_ReposPath)
            quit()
            bar.next()


if __name__ == "__main__":
    main()
