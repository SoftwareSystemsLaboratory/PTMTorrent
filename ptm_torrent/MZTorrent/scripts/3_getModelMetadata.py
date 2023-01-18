# 3_getModelMetadata.py

# Get model metadata from the saved links

import json
import os
import pickle
import time
from pathlib import PurePath

import requests
from bs4 import BeautifulSoup
from loguru import logger
from selenium import webdriver


def getHTMLRoot(url: str = "https://modelzoo.co/") -> BeautifulSoup:
    """
    get the HTML root using selenium and chromedriver
    """
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(20)  # wait a second for <div id="root"> to be fully loaded
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    root = soup.find(id="root")
    return soup


def loadList(filename: str) -> list:
    """
    load a saved list
    """
    ListFolderPath: PurePath = PurePath("./")
    ListFilePath: PurePath = PurePath(os.path.join(ListFolderPath, filename))

    with open(ListFilePath, "rb") as ListFile:
        List = pickle.load(ListFile)
    return List


def getGitLinks(soup: BeautifulSoup) -> str:
    """
    Get the Github link from a specific model page.
    """
    links = soup.find_all(
        "a", {"target": "_blank", "class": "btn btn-primary btn-get-model"}
    )
    for link in links:
        href = link.get("href")
        # print(href)
        try:
            if "https://github.com/" in href:
                if len(href.split("/")) > 5:
                    git_link = href.split("/")[:5]
                    href = "/".join(git_link)
        except:
            continue
    return href


def getMetadata(model_link: str, id: int, filepath: str) -> dict:
    """
    get the model metadata from the model page.
    """
    data = {}
    soup = getHTMLRoot(model_link)
    links = soup.find_all("div", {"class": "model-info-div box-shadow"})
    content = list(links[0].stripped_strings)
    framework = content[2] if content[2] != "-" else None
    category = content[4] if content[4] != "-" else None
    githubStar = content[6] if content[6] != "-" else None
    # logger.debug(links)

    # get the github link
    gitLink = getGitLinks(soup)
    modelOwnerURL = gitLink.split("/")[:4]
    modelOwner = modelOwnerURL[-1]
    modelURL = gitLink.split("/")[:5]
    modelName = modelURL[-1]

    modelOwnerURL = "/".join(modelOwnerURL)
    modelURL = "/".join(modelURL)

    git_api_link = f"https://api.github.com/repos/{modelOwner}/{modelName}/commits"
    request = requests.get(git_api_link)
    LatestGitCommitSHA = request.json()[0]["sha"]

    data["id"] = id
    data["ModelHub"] = {}
    data["ModelHub"]["ModelHubName"] = "Modelzoo"
    data["ModelHub"]["MetadataFilePath"] = filepath  # TODO
    data["ModelHub"]["MetadataObjectID"] = int(time.time())  # TODO
    data["ModelName"] = modelName
    data["ModelOwner"] = modelOwner
    data["ModelURL"] = model_link
    data["ModelOwnerURL"] = modelOwnerURL
    data["Datasets"] = None
    data["ModelPaperDOI"] = None
    data["LatestGitCommitSHA"] = LatestGitCommitSHA
    data["ModelTask"] = category
    data["ModelArchitecture"] = None
    # logger.debug(data)

    return data


if __name__ == "__main__":
    try:
        model_links = loadList("model_links")
    except:
        logger.error(f"The file model_links does not exist!")

    for idx, model_link in enumerate(model_links):
        filepath: str = f"../json/models_{idx}.json"
        data = getMetadata(model_link, idx, filepath)
        with open(filepath, "w") as f:
            json.dump(data, f)
        logger.info(f"Exporting JSON to {filepath} ...")
