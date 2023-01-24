from pathlib import PurePath
from typing import List

from progress.bar import Bar

import ptm_torrent.onnxmodelzoo as omz
from ptm_torrent.utils.git import cloneRepo


def cloneGitRepos(urls: List[str], gitCloneBarePath: PurePath) -> None:
    url: str
    with Bar(f"Cloning git repos to {gitCloneBarePath}...", max=len(urls)) as bar:
        for url in urls:
            cloneRepo(url, gitCloneBarePath)
            bar.next()


def main() -> None | bool:
    urls: List[str] = ["https://github.com/onnx/models"]
    cloneGitRepos(urls, omz.onnxmodelzoo_ReposPath)


if __name__ == "__main__":
    main()
