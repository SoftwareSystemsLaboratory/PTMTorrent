class ModelHub:
    def __init__(self) -> None:
        self.ModelHubName: str
        self.MetadataFilePath: str
        self.MetadataObjectID: int

    def setModelHubName(self, string: str) -> None:
        self.ModelHubName = string

    def setMetadataFilePath(self, string: str) -> None:
        self.MetadataFilePath = string

    def setMetadataObjectID(self, string: str) -> None:
        self.MetadataObjectID = string
