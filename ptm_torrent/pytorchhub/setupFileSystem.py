import ptm_torrent.pytorchhub as pyth
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    if checkFileSystem(
        rootFolderPath=pyth.rootFolderPath, subfolderPaths=pyth.subFolders
    ):
        return None
    else:
        setupFileSystem(
            rootFolderPath=pyth.rootFolderPath, subfolderPaths=pyth.subFolders
        )


if __name__ == "__main__":
    main()
