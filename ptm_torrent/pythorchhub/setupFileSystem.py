import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import checkFileSystem, setupFileSystem


def main() -> None:
    if checkFileSystem(rootFolderPath=hf.rootFolderPath, subfolderPaths=hf.subFolders):
        return None
    else:
        setupFileSystem(rootFolderPath=hf.rootFolderPath, subfolderPaths=hf.subFolders)


if __name__ == "__main__":
    main()
