# 5_createFullSetUserList.py

# Create a complete list of users (including organizations) that are listed on
# Hugging Face

from os import listdir
from os.path import join
from pathlib import PurePath

import pandas
from bs4 import BeautifulSoup, ResultSet, Tag
from pandas import DataFrame
from progress.bar import Bar
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
    name: str
    for name in names:
        try:
            if name in stor["Name"].values:
                continue
        except KeyError:
            pass

        name: str = name.replace("/", "")

        row: dict = {
            "Name": [name],
            "Type": [nameType],
            "URL": [f"https://huggingface.co/{name}"],
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
        allUsers: list = [pair[1] for pair in userModelCountMapping]
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
        stor = structureNames(
            stor=stor, names=allUsers, nameType="User", spinner=spinner
        )

    with Bar(
        "Adding model counts per user and organization to structure",
        max=len(userModelCountMapping),
    ) as bar:
        idx: int
        for idx in range(len(userModelCountMapping)):
            stor.loc[
                stor["Name"] == userModelCountMapping[idx][1], "Model Count"
            ] = int(userModelCountMapping[idx][0])
            bar.next()

    filepath: str = "../csv/users.json"
    print(f"Saving structure to {filepath} ...")
    stor = stor.sort_values(by="Model Count", ascending=False)
    stor.to_json(filepath)


if __name__ == "__main__":
    main()
