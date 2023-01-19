from concurrent.futures import ThreadPoolExecutor
from pathlib import PurePath
from typing import List

from progress.bar import Bar

from ptm_torrent.modelzoo import (expectedMZMetadataJSONFilePath,
                                  jsonMetadataPath, jsonModelMetadataPath)
from ptm_torrent.utils.fileSystem import readJSON, saveJSON
from ptm_torrent.utils.network import downloadJSON


def downloadModelMetadata(modelList: List[dict]) -> List[PurePath]:
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    paths: List[PurePath] = []

    with ThreadPoolExecutor() as executor:
        with Bar("Downloading model metadata...", max=len(modelList)) as bar:

            def _concurrurentHelper(modelSlug: str) -> None:
                url: str = f"https://modelzoo.co/api/models/{modelSlug}/"
                jsonFilePath: PurePath = PurePath(
                    f"{jsonModelMetadataPath}/{modelSlug}_metadata.json"
                )
                jsonData: dict | int = downloadJSON(url, headers)

                if type(jsonData) == int:
                    print(f"ERROR: {modelSlug}")
                    return None

                saveJSON(json=jsonData, filepath=jsonFilePath)
                paths.append(jsonFilePath)
                bar.next()

            slugs: List[str] = [model["slug"] for model in modelList]
            results = executor.map(_concurrurentHelper, slugs)

    return paths


def main() -> None | bool:
    modelMetadataJSON: List[dict] = []
    idCounter: int = 0

    modelHubJSON: dict = readJSON(jsonFilePath=expectedMZMetadataJSONFilePath)
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

    saveJSON(
        json=modelMetadataJSON, filepath=f"{jsonMetadataPath}/mz_models_metadata.json"
    )

    # print(len(mergedDF))
    # print(mergedDF.size)
    # print(mergedDF.columns)


if __name__ == "__main__":
    main()
