from pathlib import PurePath
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag

from ptm_torrent.onnx import expectedOnnxMetadataJSONPath
from ptm_torrent.utils.fileSystem import readJSON


def getTable(soup: BeautifulSoup) -> ResultSet:
    return soup.find(name="table")


def main() -> None:
    onnxJSON: List[dict] = readJSON(expectedOnnxMetadataJSONPath)

    file: str
    data: dict
    for data in onnxJSON:
        with open(data["readmePath"], "r") as htmlFile:
            soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")
            htmlFile.close()

        table: ResultSet = getTable(soup)


if __name__ == "__main__":
    main()
