from pathlib import PurePath
from typing import List

from progress.bar import Bar

import ptm_torrent.pytorchhub as pyth
from ptm_torrent.utils.fileSystem import readJSON
from ptm_torrent.utils.git import cloneRepo


def cloneGitRepos(urls: List[str], gitCloneBarePath: PurePath) -> None:
    url: str
    with Bar(f"Cloning git repos to {gitCloneBarePath}...", max=len(urls)) as bar:
        for url in urls:
            cloneRepo(url, gitCloneBarePath)
            bar.next()


def main() -> None | bool:
    json: List[dict] = readJSON(
        jsonFilePath=pyth.pytorchhub_ConcatinatedModelMetadataPath
    )
    urls: List[str] = [data["GitHubURL"] for data in json]
    cloneGitRepos(urls, pyth.pytorchhub_ReposPath)


if __name__ == "__main__":
    main()
