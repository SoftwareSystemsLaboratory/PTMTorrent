import subprocess
from pathlib import PurePath
from os import mkdir, listdir
from os.path import join

repoDirectory: PurePath = PurePath("../repos")
txtDirectory: PurePath = PurePath("../txt")

txtFiles: list = listdir(txtDirectory)

file: str
for file in txtFiles:
    if "modelIDs" in file:
        modelFile: PurePath = PurePath(join(txtDirectory, file))

with open(modelFile, "r") as mFile:
    data: list = [m.strip() for m in mFile.readlines()]
    mFile.close()

data = data[0:10]
print(data)

repo: str
for repo in data:
    origin: str = f"https://huggingface.co/{repo}"
    
    repoSplit: list = repo.split("/")
    author: str = repoSplit[0]
    projectName: str = repoSplit[1]


    authorDirectory: PurePath = PurePath(join(repoDirectory, author))
    try:
        mkdir(authorDirectory)
    except FileExistsError:
        pass

    projectDirectory: PurePath = PurePath(join(authorDirectory, projectName))
    command: str = ["git", "lfs", "clone", origin, projectDirectory]
    
    subprocess.run(command)
