import subprocess
from pathlib import PurePath
from subprocess import CompletedProcess
from typing import List
from urllib.parse import ParseResult, urlparse

# TODO: Merge cloneBareRepo() and cloneRepo() as they use the same code with
# exception of the gitCommand variable and a renamed argument


def cloneBareRepo(url: str, gitCloneBarePath: PurePath) -> CompletedProcess:
    author: str
    repo: str

    gitCommand: List[str] = ["git", "clone", "--bare", "-q"]

    parsedURL: ParseResult = urlparse(url)
    pathSplit: List[str] = parsedURL.path.strip("/").split("/")

    if len(pathSplit) == 1:
        author = parsedURL.netloc.strip()
        repo = pathSplit[0]
    else:
        author = pathSplit[0]
        repo = pathSplit[1]

    gitPath: PurePath = PurePath(f"{gitCloneBarePath}/{author}/{repo}")
    gitCommand.extend([url, gitPath])

    return subprocess.run(args=gitCommand)


def cloneRepo(url: str, rootGitClonePath: PurePath) -> CompletedProcess:
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

    gitPath: PurePath = PurePath(f"{rootGitClonePath}/{author}/{repo}")
    gitCommand.extend([url, gitPath])

    return subprocess.run(args=gitCommand)


def getLatestGitCommit(gitProjectPath: PurePath) -> str:
    gitCommand: List[str] = [
        "git",
        "--no-pager",
        "-C",
        gitProjectPath,
        "log",
        "-n 1",
        '--format="%H"',
    ]

    process: CompletedProcess = subprocess.run(
        args=gitCommand, shell=False, stdout=subprocess.PIPE
    )

    return process.stdout.decode(encoding="UTF-8").strip().replace('"', "")
