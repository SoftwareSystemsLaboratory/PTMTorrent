import ptm_torrent.modelzoo as mz
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    if checkFileSystem(rootFolderPath=mz.rootFolderPath, subfolderPaths=mz.subFolders):
        return None
    else:
        setupFileSystem(rootFolderPath=mz.rootFolderPath, subfolderPaths=mz.subFolders)


if __name__ == "__main__":
    main()
