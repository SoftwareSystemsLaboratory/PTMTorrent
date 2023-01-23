from pathlib import PurePath

import ptm_torrent as pt

rootFolderPath: PurePath = PurePath(f"{pt.dataFolderPath}/modelzoo")

reposFolderPath: PurePath = PurePath(f"{rootFolderPath}/{pt.reposFolderPath}")

jsonFolderPath: PurePath = PurePath(f"{rootFolderPath}/{pt.jsonFolderPath}")
jsonMetadataFolderPath: PurePath = PurePath(
    f"{rootFolderPath}/{pt.jsonMetadataFolderPath}"
)
jsonModelMetadataFolderPath: PurePath = PurePath(
    f"{rootFolderPath}/{pt.jsonModelMetadataFolderPath}"
)

htmlFolderPath: PurePath = PurePath(f"{rootFolderPath}/{pt.htmlFolderPath}")
htmlMetadataFolderPath: PurePath = PurePath(
    f"{rootFolderPath}/{pt.htmlMetadataFolderPath}"
)
htmlModelMetadataFolderPath: PurePath = PurePath(
    f"{rootFolderPath}/{pt.htmlModelMetadataFolderPath}"
)
