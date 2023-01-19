from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")

rootJSONPath: PurePath = PurePath("json")
jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")
jsonModelMetadataPath: PurePath = PurePath(f"{jsonMetadataPath}/models")

expectedMZMetadataJSONFilePath: PurePath = PurePath(
    f"{jsonMetadataPath}/mz_metadata.json"
)
expectedMZModelMetadataJSONFilePath: PurePath = PurePath(
    f"{jsonMetadataPath}/mz_models_metadata.json"
)
