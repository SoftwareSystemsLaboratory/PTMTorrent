# Code generated from https://app.quicktype.io/#l=schema
from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Type, TypeVar, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ModelHub:
    metadata_file_path: Optional[str] = None
    metadata_object_id: Optional[float] = None
    model_hub_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ModelHub":
        assert isinstance(obj, dict)
        metadata_file_path = from_union(
            [from_str, from_none], obj.get("MetadataFilePath")
        )
        metadata_object_id = from_union(
            [from_float, from_none], obj.get("MetadataObjectID")
        )
        model_hub_name = from_union([from_str, from_none], obj.get("ModelHubName"))
        return ModelHub(metadata_file_path, metadata_object_id, model_hub_name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.metadata_file_path is not None:
            result["MetadataFilePath"] = from_union(
                [from_str, from_none], self.metadata_file_path
            )
        if self.metadata_object_id is not None:
            result["MetadataObjectID"] = from_union(
                [to_float, from_none], self.metadata_object_id
            )
        if self.model_hub_name is not None:
            result["ModelHubName"] = from_union(
                [from_str, from_none], self.model_hub_name
            )
        return result


@dataclass
class PTMTorrent:
    datasets: Optional[List[Any]] = None
    id: Optional[float] = None
    latest_git_commit_sha: Optional[str] = None
    model_architecture: Optional[str] = None
    model_hub: Optional[ModelHub] = None
    model_name: Optional[str] = None
    model_owner: Optional[str] = None
    model_owner_url: Optional[str] = None
    model_paper_doi: Optional[str] = None
    model_task: Optional[str] = None
    model_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "PTMTorrent":
        assert isinstance(obj, dict)
        datasets = from_union(
            [lambda x: from_list(lambda x: x, x), from_none], obj.get("Datasets")
        )
        id = from_union([from_float, from_none], obj.get("id"))
        latest_git_commit_sha = from_union(
            [from_str, from_none], obj.get("LatestGitCommitSHA")
        )
        model_architecture = from_union(
            [from_str, from_none], obj.get("ModelArchitecture")
        )
        model_hub = from_union([ModelHub.from_dict, from_none], obj.get("ModelHub"))
        model_name = from_union([from_str, from_none], obj.get("ModelName"))
        model_owner = from_union([from_str, from_none], obj.get("ModelOwner"))
        model_owner_url = from_union([from_str, from_none], obj.get("ModelOwnerURL"))
        model_paper_doi = from_union([from_str, from_none], obj.get("ModelPaperDOI"))
        model_task = from_union([from_str, from_none], obj.get("ModelTask"))
        model_url = from_union([from_str, from_none], obj.get("ModelURL"))
        return PTMTorrent(
            datasets,
            id,
            latest_git_commit_sha,
            model_architecture,
            model_hub,
            model_name,
            model_owner,
            model_owner_url,
            model_paper_doi,
            model_task,
            model_url,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        if self.datasets is not None:
            result["Datasets"] = from_union(
                [lambda x: from_list(lambda x: x, x), from_none], self.datasets
            )
        if self.id is not None:
            result["id"] = from_union([to_float, from_none], self.id)
        if self.latest_git_commit_sha is not None:
            result["LatestGitCommitSHA"] = from_union(
                [from_str, from_none], self.latest_git_commit_sha
            )
        if self.model_architecture is not None:
            result["ModelArchitecture"] = from_union(
                [from_str, from_none], self.model_architecture
            )
        if self.model_hub is not None:
            result["ModelHub"] = from_union(
                [lambda x: to_class(ModelHub, x), from_none], self.model_hub
            )
        if self.model_name is not None:
            result["ModelName"] = from_union([from_str, from_none], self.model_name)
        if self.model_owner is not None:
            result["ModelOwner"] = from_union([from_str, from_none], self.model_owner)
        if self.model_owner_url is not None:
            result["ModelOwnerURL"] = from_union(
                [from_str, from_none], self.model_owner_url
            )
        if self.model_paper_doi is not None:
            result["ModelPaperDOI"] = from_union(
                [from_str, from_none], self.model_paper_doi
            )
        if self.model_task is not None:
            result["ModelTask"] = from_union([from_str, from_none], self.model_task)
        if self.model_url is not None:
            result["ModelURL"] = from_union([from_str, from_none], self.model_url)
        return result


def ptm_torrent_from_dict(s: Any) -> PTMTorrent:
    return PTMTorrent.from_dict(s)


def ptm_torrent_to_dict(x: PTMTorrent) -> Any:
    return to_class(PTMTorrent, x)
