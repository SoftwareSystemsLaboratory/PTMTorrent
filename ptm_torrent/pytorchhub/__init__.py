from pathlib import PurePath
from typing import List

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/pytorchhub")

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

pytorchhub_HubHTMLPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlMetadataFolderPath}"
)

pytorchhub_ModelHTMLPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlModelMetadataFolderPath}"
)

pytorchhub_HubHTMLMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlMetadataFolderPath}/pyth_metadata.html"
)

pytorchhub_ConcatinatedModelMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonMetadataFolderPath}/pyth_models_metadata.json"
)

pytorchhub_ReposPath: PurePath = PurePath(f"{rootFolderPath}/{reposFolderPath}")
