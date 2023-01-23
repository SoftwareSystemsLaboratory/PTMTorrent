import ptm_torrent.modelhub as mh
from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None:
    url: str = (
        "https://raw.githubusercontent.com/modelhub-ai/modelhub/master/models.json"
    )

    print(f"Downloading JSON from {url}...")
    json: dict = downloadJSON(url)

    if type(json) is int:
        print(f"Unable to download JSON from {url}.")
        quit(1)

    print(f"Saving JSON to {mh.modelhub_HubMetadataPath}")
    saveJSON(json, filepath=mh.modelhub_HubMetadataPath)


if __name__ == "__main__":
    main()
