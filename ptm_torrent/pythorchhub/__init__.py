from pathlib import PurePath
from typing import List

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/pytorchhub")

reposFolderPath: PurePath = PurePath(f"{rootFolderPath}/{pt.reposFolderPath}")

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
