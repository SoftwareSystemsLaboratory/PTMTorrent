from pathlib import PurePath
from typing import List

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/modelzoo")

reposFolderPath: PurePath = PurePath(f"{pt.reposFolderPath}")

jsonFolderPath: PurePath = PurePath(f"{pt.jsonFolderPath}")
jsonMetadataFolderPath: PurePath = PurePath(f"{pt.jsonMetadataFolderPath}")
jsonModelMetadataFolderPath: PurePath = PurePath(f"{pt.jsonModelMetadataFolderPath}")

htmlFolderPath: PurePath = PurePath(f"{pt.htmlFolderPath}")
htmlMetadataFolderPath: PurePath = PurePath(f"{pt.htmlMetadataFolderPath}")
htmlModelMetadataFolderPath: PurePath = PurePath(f"{pt.htmlModelMetadataFolderPath}")

subFolders: List[PurePath] = [
    reposFolderPath,
    jsonFolderPath,
    jsonMetadataFolderPath,
    jsonModelMetadataFolderPath,
    htmlFolderPath,
    htmlMetadataFolderPath,
    htmlModelMetadataFolderPath,
]

modelzoo_HubMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonMetadataFolderPath}/mz_metadata.json"
)

modelzoo_ModelMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonModelMetadataFolderPath}"
)

modelzoo_ConcatinatedModelMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonMetadataFolderPath}/mz_models_metadata.json"
)

modelzoo_ReposPath: PurePath = PurePath(f"{rootFolderPath}/{reposFolderPath}")
