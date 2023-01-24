from pathlib import PurePath
from typing import List

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/huggingface")

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

huggingface_HubMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonMetadataFolderPath}/hf_metadata.json"
)

huggingface_ReposPath: PurePath = PurePath(f"{rootFolderPath}/{reposFolderPath}")
