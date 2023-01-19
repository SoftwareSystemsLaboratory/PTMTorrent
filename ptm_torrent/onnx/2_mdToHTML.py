from pathlib import PurePath
from typing import List

from progress.bar import Bar

from ptm_torrent.onnx import onnxPath
from ptm_torrent.utils.fileSystem import findFiles, markdownToHTML


def main() -> None:
    readmeFiles: List[PurePath] = findFiles(globStr=f"{onnxPath}/**/README.md")

    with Bar("Converting markdown files to HTML...", max=len(readmeFiles)) as bar:
        filepath: PurePath
        for filepath in readmeFiles:
            markdownToHTML(outputDirectory="html", markdownFilepath=filepath)
            bar.next()


if __name__ == "__main__":
    main()
