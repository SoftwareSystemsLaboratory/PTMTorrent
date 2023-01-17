# 4_gitCloneModels.py

# Clone the bare Git repositories from the saved github link list.

import os
import pickle
import subprocess
from pathlib import PurePath


def cloneGitBare(linksFileName: str = "./git_links") -> None:
    '''
    Clone the bare repo from the given Github link.
    '''
    git_links = loadList(linksFileName)
    for git_link in git_links:
        gitFolderName = '/'.join(git_links[0].split('/')[-2:])
        projectDirectory: PurePath = f"../repos/{gitFolderName}"
        command: list = ["git", "clone", "--bare", git_link, projectDirectory]
        subprocess.run(command)
        git_links.remove(git_link)
        saveList(git_links, "git_links")


def saveList(List: list, filename: str) -> PurePath:
    '''
    Save a list
    '''
    ListFolderPath: PurePath = PurePath("./")
    ListFilePath: PurePath = PurePath(os.path.join(ListFolderPath, filename))

    with open(ListFilePath, "wb") as ListFile:
        pickle.dump(List, ListFile)
    return


def loadList(filename: str) -> list:
    '''
    Load a saved list
    '''
    ListFolderPath: PurePath = PurePath("./")
    ListFilePath: PurePath = PurePath(os.path.join(ListFolderPath, filename))

    with open(ListFilePath, "rb") as ListFile:
        List = pickle.load(ListFile)
    return List


if __name__ == "__main__":

    # Clone the github bare repos. Estimated to need ~100GB storage
    cloneGitBare()
