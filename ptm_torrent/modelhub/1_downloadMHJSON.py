from pathlib import PurePath

from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None:
    jsonFilePath: PurePath = PurePath("json/metadata/mh_metadata.json")
    url: str = (
        "https://raw.githubusercontent.com/modelhub-ai/modelhub/master/models.json"
    )

    json: dict = downloadJSON(url)

    if type(json) is int:
        print(f"Unable to download JSON data from {url}")

    saveJSON(json, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
