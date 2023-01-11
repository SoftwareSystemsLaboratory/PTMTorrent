class Dataset:
    def __init__(self) -> None:
        self.DatasetName: str
        self.DatasetOwner: str
        self.DatasetURL: str
        self.DatasetOwnerURL: str
        self.DatasetPaperDOIs: list = []
        self.DatasetUsages: list = []

    def setDatasetName(self, string: str) -> None:
        self.DatasetName = string

    def setDatasetOwner(self, string: str) -> None:
        self.DatasetName = string

    def setDatasetURL(self, string: str) -> None:
        self.DatasetName = string

    def setDatasetOwnerURL(self, string: str) -> None:
        self.DatasetName = string

    def setDatasetPaperDOIs(self, dois: list) -> None:
        self.DatasetPaperDOIs = dois

    def setDatasetUsages(self, usages: list) -> None:
        self.DatasetUsages = usages
