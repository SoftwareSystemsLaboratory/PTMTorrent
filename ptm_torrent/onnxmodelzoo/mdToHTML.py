from pathlib import PurePath
from typing import List

from progress.bar import Bar

import ptm_torrent.onnxmodelzoo as omz
from ptm_torrent.utils.fileSystem import findFiles, markdownToHTML


def main() -> None:
    readmeFiles: List[PurePath] = findFiles(
        globStr=f"{omz.onnxmodelzoo_GitRepoPath}/**/README.md"
    )

    onnxmodelzooREADMEPath: PurePath = readmeFiles.pop(0)

    with Bar("Converting markdown files to HTML...", max=len(readmeFiles)) as bar:

        markdownToHTML(
            outputDirectory=omz.onnxmodelzoo_HubHTMLPath,
            markdownFilepath=onnxmodelzooREADMEPath,
        )

        filepath: PurePath
        for filepath in readmeFiles:
            markdownToHTML(
                outputDirectory=omz.onnxmodelzoo_ModelHTMLPath,
                markdownFilepath=filepath,
            )
            bar.next()


if __name__ == "__main__":
    main()
