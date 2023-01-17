# Code generated from https://app.quicktype.io/#l=schema

from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Type, TypeVar, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Dataset:
    dataset_name: str
    dataset_owner: str
    dataset_owner_url: str
    dataset_url: str
    dataset_paper_doi: Optional[str] = None
    dataset_usages: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> "Dataset":
        assert isinstance(obj, dict)
        dataset_name = from_str(obj.get("DatasetName"))
        dataset_owner = from_str(obj.get("DatasetOwner"))
        dataset_owner_url = from_str(obj.get("DatasetOwnerURL"))
        dataset_url = from_str(obj.get("DatasetURL"))
        dataset_paper_doi = from_union(
            [from_str, from_none], obj.get("DatasetPaperDOI")
        )
        dataset_usages = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("DatasetUsages")
        )
        return Dataset(
            dataset_name,
            dataset_owner,
            dataset_owner_url,
            dataset_url,
            dataset_paper_doi,
            dataset_usages,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["DatasetName"] = from_str(self.dataset_name)
        result["DatasetOwner"] = from_str(self.dataset_owner)
        result["DatasetOwnerURL"] = from_str(self.dataset_owner_url)
        result["DatasetURL"] = from_str(self.dataset_url)
        if self.dataset_paper_doi is not None:
            result["DatasetPaperDOI"] = from_union(
                [from_str, from_none], self.dataset_paper_doi
            )
        if self.dataset_usages is not None:
            result["DatasetUsages"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.dataset_usages
            )
        return result


@dataclass
class ModelHub:
    metadata_file_path: str
    metadata_object_id: str
    model_hub_name: str
    model_hub_url: str

    @staticmethod
    def from_dict(obj: Any) -> "ModelHub":
        assert isinstance(obj, dict)
        metadata_file_path = from_str(obj.get("MetadataFilePath"))
        metadata_object_id = from_str(obj.get("MetadataObjectID"))
        model_hub_name = from_str(obj.get("ModelHubName"))
        model_hub_url = from_str(obj.get("ModelHubURL"))
        return ModelHub(
            metadata_file_path, metadata_object_id, model_hub_name, model_hub_url
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["MetadataFilePath"] = from_str(self.metadata_file_path)
        result["MetadataObjectID"] = from_str(self.metadata_object_id)
        result["ModelHubName"] = from_str(self.model_hub_name)
        result["ModelHubURL"] = from_str(self.model_hub_url)
        return result


@dataclass
class PTMTorrent:
    id: int
    latest_git_commit_sha: str
    model_hub: ModelHub
    model_name: str
    model_owner: str
    model_owner_url: str
    model_url: str
    datasets: Optional[List[Dataset]] = None
    model_architecture: Optional[str] = None
    model_paper_dois: Optional[List[Any]] = None
    model_task: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "PTMTorrent":
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        latest_git_commit_sha = from_str(obj.get("LatestGitCommitSHA"))
        model_hub = ModelHub.from_dict(obj.get("ModelHub"))
        model_name = from_str(obj.get("ModelName"))
        model_owner = from_str(obj.get("ModelOwner"))
        model_owner_url = from_str(obj.get("ModelOwnerURL"))
        model_url = from_str(obj.get("ModelURL"))
        datasets = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("Dataset")
        )
        model_architecture = from_union(
            [from_str, from_none], obj.get("ModelArchitecture")
        )
        model_paper_dois = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("ModelPaperDOIs")
        )
        model_task = from_union([from_str, from_none], obj.get("ModelTask"))
        return PTMTorrent(
            id,
            latest_git_commit_sha,
            model_hub,
            model_name,
            model_owner,
            model_owner_url,
            model_url,
            datasets,
            model_architecture,
            model_paper_dois,
            model_task,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["LatestGitCommitSHA"] = from_str(self.latest_git_commit_sha)
        result["ModelHub"] = to_class(ModelHub, self.model_hub)
        result["ModelName"] = from_str(self.model_name)
        result["ModelOwner"] = from_str(self.model_owner)
        result["ModelOwnerURL"] = from_str(self.model_owner_url)
        result["ModelURL"] = from_str(self.model_url)
        if self.datasets is not None:
            result["Dataset"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.datasets
            )
        if self.model_architecture is not None:
            result["ModelArchitecture"] = from_union(
                [from_str, from_none], self.model_architecture
            )
        if self.model_paper_dois is not None:
            result["ModelPaperDOIs"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.model_paper_dois
            )
        if self.model_task is not None:
            result["ModelTask"] = from_union([from_str, from_none], self.model_task)
        return result


def ptm_torrent_from_dict(s: Any) -> PTMTorrent:
    return PTMTorrent.from_dict(s)


def ptm_torrent_to_dict(x: PTMTorrent) -> Any:
    return to_class(PTMTorrent, x)
