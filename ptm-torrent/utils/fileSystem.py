from os import mkdir
from os.path import isdir
from pathlib import PurePath


def createPath(path: PurePath) -> bool:
    try:
        mkdir(path=path)
    except FileExistsError:
        pass
    return isdir(s=path)
