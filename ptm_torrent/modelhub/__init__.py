from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")
rootJSONPath: PurePath = PurePath("json")
jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")

expectedMHMetadataJSONFilePath: PurePath = PurePath("json/metadata/mh_metadata.json")
