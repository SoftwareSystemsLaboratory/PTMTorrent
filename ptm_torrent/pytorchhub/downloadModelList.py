from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

from bs4 import BeautifulSoup, ResultSet
from progress.bar import Bar
from requests import Response, get

import ptm_torrent.pytorchhub as pyth
from ptm_torrent.utils.fileSystem import readHTML, saveHTML


def getHTML(url: str, filepath: PurePath) -> None:
    resp: Response = get(url)
    saveHTML(html=resp.text, filepath=filepath)


def extractModelURLs(soup: BeautifulSoup) -> List[ParseResult]:
    baseURL: str = "https://pytorch.org"
    models: ResultSet = soup.find_all(
        name="div", attrs="col-md compact-hub-card-wrapper"
    )
    modelURIs = [model.a["href"] for model in models]

    modelURLs: List[ParseResult] = [urlparse(f"{baseURL}{uri}") for uri in modelURIs]
    return modelURLs


def main() -> None:
    pytorchHubModelListURL: str = "https://pytorch.org/hub/research-models/compact"

    print("Downloading the PyTorch Hub model list...")
    getHTML(url=pytorchHubModelListURL, filepath=pyth.pytorchhub_HubHTMLMetadataPath)

    modelHubSoup: BeautifulSoup = readHTML(
        htmlFilePath=pyth.pytorchhub_HubHTMLMetadataPath
    )

    modelURLs: List[ParseResult] = extractModelURLs(soup=modelHubSoup)

    with Bar(
        "Downloading PyTorch Hub model card HTML files...", max=len(modelURLs)
    ) as bar:
        url: ParseResult
        for url in modelURLs:
            splitPath: List[str] = url.path.strip("/").split("/")
            htmlFilepath: str = PurePath(
                f"{pyth.pytorchhub_ModelHTMLPath}/{splitPath[-1]}.html"
            )
            getHTML(url=url.geturl(), filepath=htmlFilepath)
            bar.next()


if __name__ == "__main__":
    main()
