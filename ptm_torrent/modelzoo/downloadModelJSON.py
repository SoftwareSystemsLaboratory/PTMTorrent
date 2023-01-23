from concurrent.futures import ThreadPoolExecutor
from pathlib import PurePath
from typing import List

from progress.bar import Bar

import ptm_torrent.modelzoo as mz
from ptm_torrent.utils.fileSystem import readJSON, saveJSON
from ptm_torrent.utils.network import downloadJSON


def downloadModelMetadata(modelList: List[dict]) -> List[PurePath]:
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    paths: List[PurePath] = []
    slugs: List[str] = [model["slug"] for model in modelList]

    with ThreadPoolExecutor() as executor:
        with Bar(
            "Downloading model metadata from modelzoo.co...", max=len(modelList)
        ) as bar:

            def _concurrurentHelper(modelSlug: str) -> None:
                url: str = f"https://modelzoo.co/api/models/{modelSlug}/"
                jsonFilePath: PurePath = PurePath(
                    f"{mz.modelzoo_ModelMetadataPath}/{modelSlug}_metadata.json"
                )
                jsonData: dict | int = downloadJSON(url, headers)

                saveJSON(json=jsonData, filepath=jsonFilePath)
                paths.append(jsonFilePath)
                bar.next()

            executor.map(_concurrurentHelper, slugs)

    return paths


def main() -> None | bool:
    modelMetadataJSON: List[dict] = []
    idCounter: int = 0

    modelHubJSON: dict = readJSON(jsonFilePath=mz.modelzoo_HubMetadataPath)
    modelList: List[dict] = modelHubJSON["models"]

    modelJSONPaths: List[PurePath] = downloadModelMetadata(modelList)

    modelJSONPath: PurePath
    with Bar("Concatinating JSON files...", max=len(modelJSONPaths)) as bar:
        for modelJSONPath in modelJSONPaths:
            modelJSON: dict = readJSON(jsonFilePath=modelJSONPath)
            modelJSON["id"] = idCounter
            idCounter += 1
            modelMetadataJSON.append(modelJSON)
            bar.next()

    saveJSON(json=modelMetadataJSON, filepath=mz.modelzoo_ConcatinatedModelMetadataPath)


if __name__ == "__main__":
    main()
