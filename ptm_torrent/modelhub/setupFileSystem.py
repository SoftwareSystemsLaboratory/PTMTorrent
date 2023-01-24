import ptm_torrent.modelhub as mh
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    if checkFileSystem(rootFolderPath=mh.rootFolderPath, subfolderPaths=mh.subFolders):
        return None
    else:
        setupFileSystem(rootFolderPath=mh.rootFolderPath, subfolderPaths=mh.subFolders)


if __name__ == "__main__":
    main()
