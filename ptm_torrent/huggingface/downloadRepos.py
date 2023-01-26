from typing import List

import argparse
import pathlib
from progress.bar import Bar
from progress.spinner import Spinner

import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import readJSON, testForFile
from ptm_torrent.utils.git import cloneRepo


def main(url: pathlib.Path) -> None:

    with open(url, "r") as f:
        urls = f.readlines()
    with Bar(
        f"Cloning git repos to {hf.huggingface_ReposPath}...", max=len(urls)
    ) as bar:
        url: str
        for url in urls:
            cloneRepo(url=url.strip("\n"), rootGitClonePath=hf.huggingface_ReposPath)
            bar.next()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("url_file", type=pathlib.Path)
    args = parser.parse_args()
    main(args.url_file)
