from pathlib import PurePath


class ModelHub:
    def __init__(self) -> None:
        self.ModelHubName: str
        self.MetadataFilePath: PurePath
        self.MetadataObjectID: int

    def setModelHubName(self, string: str) -> None:
        self.ModelHubName = string

    def setMetadataFilePath(self, path: PurePath) -> None:
        self.MetadataFilePath = path

    def setMetadataObjectID(self, id: int) -> None:
        self.MetadataObjectID = id
