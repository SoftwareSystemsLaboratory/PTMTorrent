# 3_downloadOrganizationPages.py

# Download all of the HTML files that contain the list of organizations on
# Hugging Face

from requests import get, Response
from bs4 import BeautifulSoup, Tag, ResultSet
from progress.bar import Bar

from time import time
from pathlib import PurePath
from os.path import join

def downloadPage(url: str = "https://huggingface.co/organizations?p=0") ->  bytes:
    resp: Response = get(url)
    
    return resp.content

def getPageCount(content: bytes)    ->  int:
    pageCount: int = 0

    soup: BeautifulSoup = BeautifulSoup(markup=content, features="lxml")
    links: ResultSet = soup.find_all(name="a")
    
    link: Tag
    for link in links:
        href: str = link.get("href")
        if "?p=" in href: 
            pageCount = int(href[3::]) if int(href[3::]) > pageCount else pageCount

    return pageCount

def saveContent(content: bytes, filename: str) ->  PurePath:
    contentFolderPath: PurePath = PurePath("../html")
    contentFilePath: PurePath = PurePath(join(contentFolderPath, filename))

    with open(contentFilePath, "wb") as contentFile:
        contentFile.write(content)
        contentFile.close()
    
    return contentFilePath


def main()  ->  None:
    unixTimeStamp: int = int(time())
    contentPage0: bytes = downloadPage()
    pageCount: int = getPageCount(contentPage0)

    with Bar("Downloading Hugging Face organization HTML pages...", max=pageCount) as bar:
        page: int
        for page in range(pageCount):
            contentFilename: str = f"organizations{page}_{unixTimeStamp}.html"
            if page == 0:
                saveContent(content=contentPage0, filename=contentFilename)
            else:
                hfURL: str = f"https://huggingface.co/organizations?p={page}"
                contentPageN: bytes = downloadPage(url=hfURL)
                saveContent(content=contentPageN, filename=contentFilename)
            bar.next()

if __name__ == "__main__":
    main()

