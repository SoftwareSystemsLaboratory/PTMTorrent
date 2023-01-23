from pathlib import PurePath
from typing import List

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/onnxmodelzoo")

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

onnxmodelzoo_ReposPath: PurePath = PurePath(f"{rootFolderPath}/{reposFolderPath}")

onnxmodelzoo_GitRepoPath: PurePath = PurePath(f"{onnxmodelzoo_ReposPath}/onnx/models")

onnxmodelzoo_HubHTMLPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlMetadataFolderPath}"
)

onnxmodelzoo_ModelHTMLPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlModelMetadataFolderPath}"
)

onnxmodelzoo_HubHTMLMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{htmlMetadataFolderPath}/README_models.html"
)

onnxmodelzoo_HubJSONMetadataPath: PurePath = PurePath(
    f"{rootFolderPath}/{jsonMetadataFolderPath}/omz_metadata.json"
)
