from pathlib import PurePath

from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None | bool:
    jsonFilePath: PurePath = PurePath("json/metadata/mz_metadata.json")

    url: str = "https://modelzoo.co/api/models/0/"
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    jsonData: dict | int = downloadJSON(url, headers)

    if type(jsonData) == int:
        return False

    saveJSON(json=jsonData, filepath=jsonFilePath)


if __name__ == "__main__":
    main()
