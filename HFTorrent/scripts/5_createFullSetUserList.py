# 5_createFullSetUserList.py

# Create a complete list of users (including organizations) that are listed on
# Hugging Face

from bs4 import BeautifulSoup, ResultSet, Tag
from pathlib import PurePath
from os import listdir
from os.path import join


def getFiles(directoryPath: PurePath)   ->  list:
    files: list = listdir(path=directoryPath)
    return [PurePath(join(directoryPath, f)) for f in files]

def getUsername(filepath: PurePath, className: str) ->  str:
    htmlFile: bytes = open(filepath, "rb").read()
    soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")
    
    users: ResultSet = soup.find_all(name="a", attrs={"class", className})
    user: Tag
    for user in users:
        print(user.get("href"))


def main()  ->  None:
    usersDirectory: PurePath = PurePath("../html/users")
    organizationsDirectorty: PurePath = PurePath("../html/organizations")

    usersFiles: list = getFiles(directoryPath=usersDirectory)
    organizationsFiles: list = getFiles(directoryPath=organizationsDirectorty)

    file: PurePath
    for file in usersFiles:
        getUsername(file, "flex items-center flex-1 p-3")

if __name__ == "__main__":
    main()
