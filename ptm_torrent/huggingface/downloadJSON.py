import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def main() -> None:
    url: str = "https://huggingface.co/api/models?full=true&config=true"

    print(f"Downloading JSON from {url}...")
    json: dict = downloadJSON(url)

    if type(json) is int:
        print(f"Unable to download JSON from {url}.")
        quit(1)

    print(f"Saving JSON to {hf.huggingface_HubMetadataPath}")
    saveJSON(json, filepath=hf.huggingface_HubMetadataPath)


if __name__ == "__main__":
    main()
