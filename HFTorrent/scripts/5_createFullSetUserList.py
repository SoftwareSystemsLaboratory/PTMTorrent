# 5_createFullSetUserList.py

# Create a complete list of users (including organizations) that are listed on
# Hugging Face

from os import listdir
from os.path import join
from pathlib import PurePath

import pandas
from bs4 import BeautifulSoup, ResultSet, Tag
from pandas import DataFrame
from progress.spinner import Spinner


def getFiles(directoryPath: PurePath) -> list:
    files: list = listdir(path=directoryPath)
    return [PurePath(join(directoryPath, f)) for f in files]


def getUsername(filepath: PurePath, className: str) -> list:
    data: list = []
    htmlFile: bytes = open(filepath, "rb").read()
    soup: BeautifulSoup = BeautifulSoup(markup=htmlFile, features="lxml")

    users: ResultSet = soup.find_all(name="a", attrs={"class", className})
    user: Tag
    for user in users:
        data.append(user.get("href"))

    return data


def structureNames(
    stor: DataFrame, names: list, nameType: str, spinner: Spinner
) -> DataFrame:
    names: set = set(names)
    name: str
    for name in names:
        row: dict = {
            "Name": [name.replace("/", "")],
            "Type": [nameType],
            "URL": [f"https://huggingface.co{name}"],
            "Model Count": 0,
        }
        tempDF: DataFrame = DataFrame(row, index=[0])
        stor = pandas.concat([stor, tempDF], ignore_index=True)
        spinner.next()
    return stor


def main() -> None:
    stor: DataFrame = DataFrame()
    userNames: list = []
    organizationNames: list = []

    usersDirectory: PurePath = PurePath("../html/users")
    organizationsDirectory: PurePath = PurePath("../html/organizations")
    txtDirectory: PurePath = PurePath("../txt")

    usersFiles: list = getFiles(directoryPath=usersDirectory)
    organizationsFiles: list = getFiles(directoryPath=organizationsDirectory)
    txtFiles: list = getFiles(directoryPath=txtDirectory)

    userModelCountMappingFile: PurePath
    txt: PurePath
    for txt in txtFiles:
        if "ModelCount" in txt.name:
            userModelCountMappingFile = txt
            break

    with open(userModelCountMappingFile, "r") as txtFile:
        userModelCountMapping: list = txtFile.readlines()
        userModelCountMapping = [
            tuple(m.strip().split(" ")) for m in userModelCountMapping
        ]
        txtFile.close()

    with Spinner(
        "Finding all usernames and organization names on HuggingFace..."
    ) as spinner:
        file: PurePath
        for file in usersFiles:
            userNames.extend(getUsername(file, "flex items-center flex-1 p-3"))
            spinner.next()

        for file in organizationsFiles:
            organizationNames.extend(
                getUsername(file, "flex items-center flex-1 overflow-hidden p-3")
            )
            spinner.next()

    with Spinner("Structuring usernames and organization names...") as spinner:
        stor = structureNames(
            stor=stor, names=userNames, nameType="User", spinner=spinner
        )
        stor = structureNames(
            stor=stor, names=organizationNames, nameType="Organizaton", spinner=spinner
        )

    pair: tuple
    for pair in userModelCountMapping:
        stor.loc[stor["Name"] == pair[1], "Model Count"] = pair[0]

    stor.to_csv("test.csv")


if __name__ == "__main__":
    main()
