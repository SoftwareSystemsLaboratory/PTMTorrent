# 2_downloadModelPage.py

# Download all of the HTML files and get github links for each model

import os
import pickle
import time
from pathlib import PurePath

from bs4 import BeautifulSoup
from loguru import logger
from selenium import webdriver


def getHTMLRoot(url: str = "https://modelzoo.co/") -> BeautifulSoup:
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(20)  # wait 20 second for <div id="root"> to be fully loaded
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    # root = soup.find(id='root')
    return soup


def saveContent(content, filename: str) -> PurePath:
    contentFolderPath: PurePath = PurePath("./")
    contentFilePath: PurePath = PurePath(os.path.join(contentFolderPath, filename))

    with open(contentFilePath, "w") as contentFile:
        contentFile.write(str(content))
        contentFile.close()

    return contentFilePath


def saveList(List: list, filename: str) -> PurePath:
    ListFolderPath: PurePath = PurePath("./")
    ListFilePath: PurePath = PurePath(os.path.join(ListFolderPath, filename))

    with open(ListFilePath, "wb") as ListFile:
        pickle.dump(List, ListFile)
    return


def loadList(filename: str) -> list:
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


def getGitLinks(model_name: str, modelLinks: list, git_links: list) -> list:
    model_link: str = f"https://modelzoo.co{model_name}"
    modelLinks.append(model_link)
    saveList(modelLinks, "./model_links")
    soup = getHTMLRoot(model_link)
    try:
        saveContent(soup, f"../html/{model_name[7:]}_{int(time.time())}")
    except:
        logger.debug(f"Warning: saveContent failed for {model_link}!")
    # model_cnt += 1
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
                if href not in git_links:
                    git_links.append(href)
                    logger.info(f"Get the git link: {href}")
                else:
                    logger.debug(f"{href} already in git_links...")

                # break
        except:
            continue
    # saveContent(git_links, "git_links.txt")
    saveList(git_links, "git_links")
    # saveList(git_links, "git_links_backup")
    return git_links


def getModelPages(resume: bool = False) -> None:
    if not resume:
        logger.info(f"Creating new file for model_links...")
        soup = getHTMLRoot(url="https://modelzoo.co/")
        pageCount = 0
        links = soup.find_all("a")
        model_names = []
        for link in links:
            href = link.get("href")
            model_name = link.get("title")
            try:
                if "/model/" in href and href not in model_names:
                    model_names.append(href)
                    pageCount += 1
                    # logger.info(href)
            except:
                continue
        logger.info(f"page count: {pageCount}")
        saveList(model_names, "./model_names")
        # saveList(model_names, "./model_names_backup")
    else:
        logger.info(f"Loading from existing model_names...")
        model_names = loadList("./model_names")

    model_cnt = 0
    git_links = []
    modelLinks = []
    # logger.debug(model_links)

    for model_name in model_names:
        # logger.debug(model_name, git_links)
        git_Links = getGitLinks(model_name, modelLinks, git_links)
        model_cnt += 1
        # del model_names[0]
        model_names.remove(model_name)
        saveList(model_names, "./model_names")
        # For testing only
        # if model_cnt == 2:
        #     return
    return


if __name__ == "__main__":

    # Get the github links and model page for each model
    getModelPages(resume=False)  # Set resume=True if the process was crashed
