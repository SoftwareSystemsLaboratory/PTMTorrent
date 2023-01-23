from pathlib import PurePath
from typing import List

from progress.spinner import Spinner

from ptm_torrent.modelhub import rootFolderPath
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    checkFileSystem(rootFolderName=rootFolderPath)

    pathNames: List[str] = ["repos", "json", "json/metadata"]
    paths: List[PurePath] = [PurePath(pn) for pn in pathNames]

    with Spinner("Creating file directories...") as spinner:
        path: PurePath
        for path in paths:
            createPath(path)


if __name__ == "__main__":
    main()
