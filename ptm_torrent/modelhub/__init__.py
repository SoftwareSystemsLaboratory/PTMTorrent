from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")
rootJSONPath: PurePath = PurePath("json")
jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")

expectedMHMetadataJSONFilePath: PurePath = PurePath(
    f"{jsonMetadataPath}/mh_metadata.json"
)
