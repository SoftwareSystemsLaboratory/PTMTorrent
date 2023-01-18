import subprocess
from pathlib import PurePath
from subprocess import CompletedProcess
from typing import List
from urllib.parse import ParseResult, urlparse


def cloneRepo(url: str, rootPath: PurePath) -> CompletedProcess:
    author: str
    repo: str

    gitCommand: List[str] = ["git", "clone", "-q"]

    parsedURL: ParseResult = urlparse(url)
    pathSplit: List[str] = parsedURL.path.strip("/").split("/")

    if len(pathSplit) == 1:
        author = parsedURL.netloc.strip()
        repo = pathSplit[0]
    else:
        author = pathSplit[0]
        repo = pathSplit[1]

    gitPath: PurePath = PurePath(f"{rootPath}/{author}/{repo}")
    gitCommand.extend([url, gitPath])

    return subprocess.run(args=gitCommand)


cloneRepo("https://github.com/NicholasSynovic/setup", "repos")
