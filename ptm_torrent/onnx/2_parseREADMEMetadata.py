from json import loads
from pathlib import PurePath
from typing import List

from mistletoe import Document
from mistletoe.ast_renderer import ASTRenderer
from progress.bar import Bar

from ptm_torrent.onnx import onnxPath
from ptm_torrent.utils.fileSystem import findFiles


def findREADMEs() -> List[PurePath]:
    return findFiles(globStr=f"{onnxPath}/**/README.md")


def readme2AST(filepath: PurePath) -> dict:
    with open(filepath, "r") as readmeFile:
        with ASTRenderer() as astRenderer:
            document: Document = Document(readmeFile)
            renderedAST: str = astRenderer.render(document)
        readmeFile.close()
    return loads(renderedAST)


def findTables(ast: dict) -> dict:
    pass


def main() -> None:
    asts: List[dict] = []

    readmePaths: List[PurePath] = findREADMEs()

    with Bar("Converting README metadata files to AST...", max=len(readmePaths)) as bar:
        path: PurePath
        for path in readmePaths:
            asts.append(readme2AST(filepath=path))
            bar.next()


if __name__ == "__main__":
    main()
