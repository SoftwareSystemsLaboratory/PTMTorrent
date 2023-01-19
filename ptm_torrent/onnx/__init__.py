from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")

rootJSONPath: PurePath = PurePath("json")
onnxPath: PurePath = PurePath(f"{rootGitClonePath}/onnx/models")

jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")

expectedMZMetadataJSONFilePath: PurePath = PurePath(
    f"{jsonMetadataPath}/mz_metadata.json"
)
expectedMZModelMetadataJSONFilePath: PurePath = PurePath(
    f"{jsonMetadataPath}/mz_models_metadata.json"
)
