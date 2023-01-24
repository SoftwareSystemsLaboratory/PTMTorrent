from pathlib import PurePath
from typing import List
from urllib.parse import ParseResult, urlparse

from bs4 import BeautifulSoup, ResultSet
from requests import Response, get

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
    pytorchHubHTMLPath: PurePath = PurePath("html/pytorchhub_metadata.html")

    getHTML(url=pytorchHubModelListURL, filepath=pytorchHubHTMLPath)

    modelHubSoup: BeautifulSoup = readHTML(htmlFilePath=pytorchHubHTMLPath)

    modelURLs: List[ParseResult] = extractModelURLs(soup=modelHubSoup)

    url: ParseResult
    for url in modelURLs:
        splitPath: List[str] = url.path.strip("/").split("/")
        htmlFilepath: str = PurePath(f"html/models/{splitPath[-1]}.html")
        getHTML(url=url.geturl(), filepath=htmlFilepath)


if __name__ == "__main__":
    main()
