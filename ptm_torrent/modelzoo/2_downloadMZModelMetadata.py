from pathlib import PurePath
from typing import List

from progress.bar import Bar

from ptm_torrent.utils.fileSystem import readJSON, saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None | bool:
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    jsonFilePath: PurePath = PurePath("json/metadata/mz_metadata.json")

    jsonData: dict = readJSON(jsonFilePath)
    modelList: List[dict] = jsonData["models"]

    with Bar("Downloading model metadata...", max=len(modelList)) as bar:
        modelData: dict
        for modelData in modelList:
            modelSlug: str = modelData["slug"]

            url: str = f"https://modelzoo.co/api/models/{modelSlug}/"
            jsonFilePath: PurePath = PurePath(
                f"json/metadata/{modelSlug}_metadata.json"
            )

            jsonData: dict | int = downloadJSON(url, headers)

            if type(jsonData) == int:
                print(f"ERROR: {modelSlug}")
                continue

            saveJSON(json=jsonData, filepath=jsonFilePath)

            bar.next()


if __name__ == "__main__":
    main()
