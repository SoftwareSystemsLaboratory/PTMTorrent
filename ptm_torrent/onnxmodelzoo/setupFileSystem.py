import ptm_torrent.onnxmodelzoo as omz
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    if checkFileSystem(
        rootFolderPath=omz.rootFolderPath, subfolderPaths=omz.subFolders
    ):
        return None
    else:
        setupFileSystem(
            rootFolderPath=omz.rootFolderPath, subfolderPaths=omz.subFolders
        )


if __name__ == "__main__":
    main()
