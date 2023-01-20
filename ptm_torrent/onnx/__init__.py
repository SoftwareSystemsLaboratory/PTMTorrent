from pathlib import PurePath

rootGitClonePath: PurePath = PurePath("repos")
onnxPath: PurePath = PurePath(f"{rootGitClonePath}/onnx/models")

rootJSONPath: PurePath = PurePath("json")
rootHTMLPath: PurePath = PurePath("html")

jsonMetadataPath: PurePath = PurePath(f"{rootJSONPath}/metadata")

expectedOnnxHTMLPath: PurePath = PurePath(f"{rootHTMLPath}/README_models.html")
