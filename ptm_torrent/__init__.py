from pathlib import PurePath

from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem

dataFolderPath: PurePath = PurePath("data")

reposFolderPath: PurePath = PurePath("repos")

jsonFolderPath: PurePath = PurePath("json")
jsonMetadataFolderPath: PurePath = PurePath(f"{jsonFolderPath}/metadata")
jsonModelMetadataFolderPath: PurePath = PurePath(f"{jsonMetadataFolderPath}/models")

htmlFolderPath: PurePath = PurePath("html")
htmlMetadataFolderPath: PurePath = PurePath(f"{htmlFolderPath}/metadata")
htmlModelMetadataFolderPath: PurePath = PurePath(f"{htmlMetadataFolderPath}/models")
