from os import listdir
from pathlib import PurePath
from typing import List

from bs4 import BeautifulSoup, Tag

import ptm_torrent.pytorchhub as pyth
from ptm_torrent.utils.fileSystem import readHTML, saveJSON


def extractURL(soup: BeautifulSoup, buttonClass: str) -> str | None:
    button: Tag = soup.find(name="button", attrs={"class": buttonClass})
    try:
        return button.parent.get("href")
    except AttributeError:
        return None


def getModelName(soup: BeautifulSoup) -> str:
    return soup.find(name="h1").text.strip()


def getModelAuthor(soup: BeautifulSoup) -> str:
    return soup.find(name="p", attrs={"class": "detail-lead"}).text.strip()[3::]


def getModelDescription(soup: BeautifulSoup) -> str:
    return soup.find(name="p", attrs={"class": "lead-summary"}).text.strip()


def buildJSON(id: int, soup: BeautifulSoup) -> dict:
    modelName: str = getModelName(soup)
    modelAuthor: str = getModelAuthor(soup)
    modelDescription: str = getModelDescription(soup)
    modelURL: str = ""
    githubURL: str = extractURL(soup=soup, buttonClass="detail-github-link")
    colabURL: str = extractURL(soup=soup, buttonClass="detail-colab-link")
    demoURL: str = extractURL(soup=soup, buttonClass="detail-web-demo-link")

    data: dict = {
        "id": id,
        "ModelName": modelName,
        "ModelAuthor": modelAuthor,
        "ModelDescription": modelDescription,
        "ModelURL": modelURL,
        "GitHubURL": githubURL,
        "ColabURL": colabURL,
        "DemoURL": demoURL,
    }
    return data


def main() -> None:
    json: List[dict] = []

    htmlFiles: List[PurePath] = [
        PurePath(f"{pyth.pytorchhub_ModelHTMLPath}/{path}")
        for path in listdir(path=pyth.pytorchhub_ModelHTMLPath)
    ]

    idx: int
    for idx in range(len(htmlFiles)):
        soup: BeautifulSoup = readHTML(htmlFilePath=htmlFiles[idx])
        data: dict = buildJSON(id=idx, soup=soup)
        json.append(data)

    print(f"Saving data to {pyth.pytorchhub_ConcatinatedModelMetadataPath}")
    saveJSON(json=json, filepath=pyth.pytorchhub_ConcatinatedModelMetadataPath)


if __name__ == "__main__":
    main()
