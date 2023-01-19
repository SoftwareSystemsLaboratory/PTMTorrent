from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")
rootJSONPath: PurePath = PurePath("json")
jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")

expectedMZMetadataJSONFilePath: PurePath = PurePath("json/metadata/mz_metadata.json")
