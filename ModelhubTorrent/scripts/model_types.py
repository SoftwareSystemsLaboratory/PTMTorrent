"""
types for modelhub config and schema as a python type
"""
from typing import TypedDict, Dict, Literal, List


class TModelHubMeta(TypedDict):
    """
    Typed meta field in a typical modelhub->model->config.json
    """

    name: str
    application_area: str
    task: str
    task_extended: str
    data_type: str
    data_source: str


class TModelHubPublication(TypedDict):
    """
    Typed publication field in a typical modelhub->model->config.json
    """

    title: str
    source: str
    year: int
    authors: str  # comma separated
    abstract: str
    url: str
    google_scholar: str
    bibtex: str


class TModelHubModel(TypedDict):
    """
    Typed model field in a typical modelhub->model->config.json
    """

    description: str
    provenance: str
    architecture: str
    learning_type: str
    format: str
    # todo: granular i/o types?
    io: Dict[Literal["input", "output"], str]


class TModelHubConfig(TypedDict):
    """Types for a  typical modelhub->model->config.json file"""

    id: str
    meta: TModelHubMeta
    publication: TModelHubPublication
    model: TModelHubModel

    # ignore this property, looks pretty much useless as it has 10 entiries in the "top 5" category
    modelhub: dict


class TModelHub(TypedDict):
    """
    Types for the model hub object in the model schema
    """

    ModelHubName: str
    MetadataFilePath: str
    MetadataObjectID: str


class TDataset(TypedDict):
    """
    Types for the dataet object in the model schema
    """

    DatasetName: str
    DatasetOwner: str
    DatasetURL: str
    DatasetOwnerURL: str
    DatasetPaperDOI: str
    DatasetUsages: List[str]


class TModelSchema(TypedDict):
    """
    The model schema as a python typed dict
    """

    id: int
    ModelHub: TModelHub
    ModelName: str
    ModelOwner: str
    ModelURL: str
    ModelOwnerURL: str
    Datasets: List[TDataset]
    ModelPaperDOI: str
    LatestGitCommitSHA: str
    ModelTask: str
    ModelArchitecture: str


class TModelResponse(TypedDict):
    """
    Types for the model index items
    """

    id: str
    name: str
    task_extended: str
    github: str
    github_branch: str
    backend: List[str]
