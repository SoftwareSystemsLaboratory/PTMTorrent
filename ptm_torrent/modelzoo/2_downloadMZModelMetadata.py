from concurrent.futures import ThreadPoolExecutor
from pathlib import PurePath
from typing import List

from progress.bar import Bar

from ptm_torrent.modelzoo import expectedMZMetadataJSONFilePath
from ptm_torrent.utils.fileSystem import readJSON, saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None | bool:
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    jsonData: dict = readJSON(jsonFilePath=expectedMZMetadataJSONFilePath)
    modelList: List[dict] = jsonData["models"]

    with ThreadPoolExecutor() as executor:
        with Bar("Downloading model metadata...", max=len(modelList)) as bar:

            def _concurrurentHelper(modelSlug: str) -> None:
                url: str = f"https://modelzoo.co/api/models/{modelSlug}/"
                jsonFilePath: PurePath = PurePath(
                    f"json/metadata/{modelSlug}_metadata.json"
                )
                jsonData: dict | int = downloadJSON(url, headers)

                if type(jsonData) == int:
                    print(f"ERROR: {modelSlug}")
                    return None

                saveJSON(json=jsonData, filepath=jsonFilePath)
                bar.next()

            slugs: List[str] = [model["slug"] for model in modelList]
            results = executor.map(_concurrurentHelper, slugs)


if __name__ == "__main__":
    main()
