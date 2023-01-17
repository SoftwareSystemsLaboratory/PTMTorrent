"""
Helpers for converting a fetched model info  to the desired schema
"""
from model_types import TModelHubConfig, TModelSchema


class Model:
    """
    Model class to generate a dictionary matching the required schema
    """

    def numeric_id(self, arg: str):
        """
        convert a string based id to numeric
        I hope there's no collisions here
        """

        return hash(arg)

    def __init__(self, config: TModelHubConfig, path: str, url: str, sha: str) -> None:
        self.config = config
        self.path = path
        self.url = url
        self.sha = sha

    @property
    def as_json(self) -> TModelSchema:
        """
        converts a modelhub config type to the schema
        """
        return {
            "id": self.numeric_id(self.config["id"]),
            "Datasets": [
                # modelhub does not provide dataset information
            ],
            "LatestGitCommitSHA": self.sha,
            "ModelArchitecture": self.config["model"]["architecture"],
            "ModelHub": {
                "ModelHubName": "modelhub (modelhub.ai)",
                "MetadataFilePath": str(self.path),
                "MetadataObjectID": self.numeric_id(self.config["id"]),
            },
            "ModelName": self.config["meta"]["name"],
            "ModelOwner": self.config["publication"]["authors"],
            "ModelOwnerURL": self.config["publication"]["google_scholar"],
            "ModelPaperDOI": "",
            "ModelTask": self.config["meta"]["task"],
            "ModelURL": self.url,
        }
