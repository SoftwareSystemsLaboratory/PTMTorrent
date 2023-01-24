import ptm_torrent.modelzoo as mz
from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None | bool:

    url: str = "https://modelzoo.co/api/models/0/"
    headers: dict = {"User-Agent": "PTMTorrent", "Referer": "https://modelzoo.co/"}

    print(f"Downloading JSON from {url}...")
    jsonData: dict | int = downloadJSON(url, headers)

    if type(jsonData) == int:
        print(f"Unable to download JSON from {url}.")
        return False

    print(f"Saving JSON to {mz.modelzoo_HubMetadataPath}")
    saveJSON(json=jsonData, filepath=mz.modelzoo_HubMetadataPath)


if __name__ == "__main__":
    main()
