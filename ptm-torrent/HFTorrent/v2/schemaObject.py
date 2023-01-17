from datasetObject import Dataset
from mhObject import ModelHub


class Schema:
    def __init__(self) -> None:
        self.id: int
        self.ModelHub: ModelHub
        self.ModelName: str
        self.ModelOwner: str
        self.ModelURL: str
        self.ModelOwnerURL: str
        self.Datasets: list[Dataset] = []
        self.ModelPaperDOIs: list[str] = []
        self.LatestGitCommitSHA: str
        self.ModelTasks: list[str] = []
        self.ModelArchitecture: str

    def setID(self, id: int) -> None:
        self.id = id

    def setModelHub(self, mh: ModelHub) -> None:
        self.ModelHub = mh

    def setModelName(self, string: str) -> None:
        self.ModelName = string

    def setModelOwner(self, string: str) -> None:
        self.ModelOwner = string

    def setModelOwnerURL(self, string: str) -> None:
        self.ModelOwnerURL = string

    def setModelURL(self, string: str) -> None:
        self.ModelURL = string

    def setDatasets(self, list: list[Dataset]) -> None:
        self.Datasets = list

    def setModelPaperDOIs(self, list: list[str]) -> None:
        self.Datasets = list

    def setLatestGitCommitSHA(self, string: str) -> None:
        self.LatestGitCommitSHA = string

    def setModelTasks(self, list: list[str]) -> None:
        self.ModelTasks = list

    def setModelArchitecture(self, string: str) -> None:
        self.ModelArchitecture = string
