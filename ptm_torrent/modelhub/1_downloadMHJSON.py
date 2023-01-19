from pathlib import PurePath

from ptm_torrent.modelhub import expectedMHMetadataJSONFilePath
from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None:
    url: str = (
        "https://raw.githubusercontent.com/modelhub-ai/modelhub/master/models.json"
    )

    json: dict = downloadJSON(url)

    if type(json) is int:
        print(f"Unable to download JSON data from {url}")

    saveJSON(json, filepath=expectedMHMetadataJSONFilePath)


if __name__ == "__main__":
    main()
