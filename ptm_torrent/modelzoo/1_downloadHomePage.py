import time
from pathlib import PurePath

from requests import Response, Session, get

from ptm_torrent.utils.fileSystem import saveHTML
from ptm_torrent.utils.network import downloadHTML


def main() -> None:
    url: str = "https://modelzoo.co/api/models/50/"

    resp: Response = get(url)
    resp.json()

    quit()

    # html: str | int = downloadHTML(url)

    if type(html) is int:
        print(f"Unable to download HTML data from {url}")

    # saveHTML(html, filepath=)


if __name__ == "__main__":
    main()
