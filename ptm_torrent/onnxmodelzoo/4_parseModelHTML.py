from pathlib import PurePath
from typing import List

import pandas
from pandas import DataFrame, Series
from progress.bar import Bar

from ptm_torrent.onnxmodelzoo import expectedOnnxMetadataJSONPath
from ptm_torrent.utils.fileSystem import readJSON, saveJSON


def prepareData(
    dfs: List[DataFrame], readmePath: PurePath, firstColumn: str = "Model"
) -> DataFrame:
    validDFs: List[DataFrame] = []

    df: DataFrame
    for df in dfs:
        df.columns = [pair[0] for pair in df.columns]
        df["readmePath"] = readmePath

        if df.columns.__contains__(firstColumn):
            rowCount: int = len(df)
            idx: int
            for idx in range(rowCount):
                if df.loc[idx, firstColumn][0][0] == ">":
                    df.drop(index=idx, inplace=True)
            validDFs.append(df)

    data: DataFrame = pandas.concat(objs=dfs, ignore_index=True)

    return data


def extractTextFromPair(
    df: DataFrame, labels: List[str], pairIndex: int = 0, drop: bool = False
) -> DataFrame:
    rowCount: int = len(df)
    idx: int
    for idx in range(rowCount):
        label: str
        for label in labels:
            try:
                df.loc[idx, label] = df.loc[idx, label][pairIndex]
            except TypeError:
                if drop:
                    df.drop(index=idx, inplace=True)
                continue
    return df


def mergeColumns(
    df: DataFrame, column1: str, column2: str, newColumn: str
) -> DataFrame:
    df[column1].fillna(value="", inplace=True)
    df[column2].fillna(value="", inplace=True)
    df[newColumn] = df[column1] + df[column2]
    df.drop(columns=[column1, column2], inplace=True)

    return df


def createJSON(df: DataFrame, category: str) -> List[dict]:
    json: List[dict] = []
    rowCount: int = len(df)

    idx: int
    for idx in range(rowCount):
        data: dict = {}

        row: Series = df.loc[idx]
        readmePath: PurePath = row["readmePath"]

        data["id"] = idx
        data["Model"] = row["Model"]
        data["ModelSize"] = row["Download"][0]
        data["ModelPath"] = f'{readmePath}/{row["Download"][1]}'
        data["ONNXVersion"] = row["ONNX version"]
        data[r"Top-1% Accuracy"] = row["Top-1 accuracy (%)"]
        data[r"Top-5% Accuracy"] = row["Top-5 accuracy (%)"]
        data["Accuracy"] = row["Accuracy"]
        data["mAP"] = row["mAP"]
        data["mIOU"] = row["mIOU  (%)"]
        data["Mean IoU"] = row["Mean IoU"]
        data["LFW * accuracy (%)"] = row["LFW * accuracy (%)"]
        data["CFP-FF * accuracy (%)"] = row["CFP-FF * accuracy (%)"]
        data["CFP-FP * accuracy (%)"] = row["CFP-FP * accuracy (%)"]
        data["AgeDB-30 * accuracy (%)"] = row["AgeDB-30 * accuracy (%)"]
        data["Dataset"] = row["Dataset"]
        data["OpsetVersion"] = row["OpsetVersion"]
        data["Top-1 Error (%)"] = row["Top-1 Error (%)"]

        try:
            data["ModelSampleSize"] = row["Download (with sample test data)"][0]
        except TypeError:
            data["ModelSampleSize"] = None

        try:
            data[
                "ModelSamplePath"
            ] = f'{readmePath}/{row["Download (with sample test data)"][1]}'
        except TypeError:
            data["ModelSamplePath"] = None

        json.append(data)

    return json


def main() -> None:
    tables: List[DataFrame] = []
    tableLabels: List[str] = [
        "ONNX version",
        "Opset version",
        "Opset Version",
        "Top-1 accuracy (%)",
        "Top-5 accuracy (%)",
        "Top-1 error",
        "TOP-1 ERROR",
        "Top-5 error",
        "Accuracy",
        "mAP",
        "mIOU  (%)",
        "Filename",
        "Size",
        "Details",
        "Mean IoU",
        "LFW * accuracy (%)",
        "CFP-FF * accuracy (%)",
        "CFP-FP * accuracy (%)",
        "AgeDB-30 * accuracy (%)",
        "Dataset",
    ]

    modelHubMetadata: List[dict] = readJSON(jsonFilePath=expectedOnnxMetadataJSONPath)

    modelREADMEPaths: List[PurePath] = [
        PurePath(metadata["ModelREADMEPath"])
        for metadata in modelHubMetadata
        if metadata["ModelREADMEPath"] != None
    ]
    repoREADMEPaths: List[PurePath] = [
        PurePath(metadata["RepoREADMEPath"])
        for metadata in modelHubMetadata
        if metadata["RepoREADMEPath"] != None
    ]

    with Bar(
        "Converting model HTML data into DataFrames...", max=len(modelREADMEPaths)
    ) as bar:

        path: PurePath
        for pathPair in list(zip(modelREADMEPaths, repoREADMEPaths)):
            modelTables: List[DataFrame] = pandas.read_html(
                io=pathPair[0], extract_links="all"
            )

            tables.append(prepareData(dfs=modelTables, readmePath=pathPair[1]))
            bar.next()

    data: DataFrame = pandas.concat(objs=tables, ignore_index=True)
    data = extractTextFromPair(df=data, labels=["Model"], drop=True)
    data.reset_index(drop=True, inplace=True)
    data = extractTextFromPair(df=data, labels=tableLabels)

    data = mergeColumns(
        df=data,
        column1="Opset version",
        column2="Opset Version",
        newColumn="OpsetVersion",
    )

    data = mergeColumns(
        df=data,
        column1="Top-1 error",
        column2="TOP-1 ERROR",
        newColumn=r"Top-1 Error (%)",
    )

    json: List[dict] = createJSON(df=data, category="test")

    saveJSON(json, filepath="test.json")


if __name__ == "__main__":
    main()
