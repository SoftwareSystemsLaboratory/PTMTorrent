import csv
import glob
import json

import mistletoe
from mistletoe.ast_renderer import ASTRenderer

# Maybe generalize dfs with higher-order functions

# Finds all Table Nodes in AST
def dfs_table_find(file_as_json):
    # DFS to find Tables
    tables = []
    stack = [file_as_json]
    while stack:
        curr_node = stack.pop()
        # Finds a Table and then stops going down this branch.
        if curr_node["type"] == "Table":
            print("Table found")
            tables.append(curr_node)
            continue
        if "children" in curr_node:
            stack.extend(curr_node["children"])
    return tables


# Parses all Rows
def dfs_row_parse(children, header=False):
    # DFS to find Tables
    cells = []
    children = children["children"]
    stack = children
    while stack:
        curr_node = stack.pop()
        # Finds a Table and then stops going down this branch.
        if not header:
            if curr_node["type"] == "Link":
                cells.append(
                    {
                        "target": curr_node["target"],
                        "content": curr_node["children"][0]["content"],
                    }
                )
                continue
        if curr_node["type"] == "TableCell" and not curr_node["children"]:
            cells.append(None)
        if "content" in curr_node:
            cells.append(curr_node["content"])
        if "children" in curr_node:
            stack.extend(curr_node["children"])

    return cells[::-1]


def dfs_table_parse(table):
    # DFS to find Tables
    cells = []
    stack = [table]
    while stack:
        curr_node = stack.pop()
        # Finds a Table and then stops going down this branch.
        if curr_node["type"] == "TableRow":
            cells.append(curr_node)
            continue
        if "content" in curr_node:
            cells.append(curr_node["content"])
        if "children" in curr_node:
            stack.extend(curr_node["children"])
    return cells[::-1]


def create_metadata(idx, model, offset, manual=False):
    if not manual:
        gen_metadata = create_general_metadata(idx, model, offset)
        specific_metadata = create_specific_metadata(model)
    else:
        gen_metadata = create_general_metadata_manual(idx, model, offset)
        specific_metadata = create_specific_metadata_manual(model)

    filename = f"{gen_metadata['id']}_{gen_metadata['ModelName']}.json"
    with open(f"./general_metadata/{filename}", "w") as f:
        gen_metadata["ModelHub"]["MetadataFilePath"] = f"onnx_metadata/{filename}"
        f.write(json.dumps(gen_metadata))

    with open(f"./onnx_metadata/{filename}", "w") as f:
        f.write(json.dumps(specific_metadata))


def create_general_metadata(idx, model, offset):
    joined_path = "/".join(model["path_in_repo"].split("/")[2:-1])
    target = model["Download"]["target"]
    url = f"https://github.com/onnx/models/blob/main/{joined_path}/{target}"

    gen_metadata = {
        "id": idx + offset,
        "ModelHub": {
            "ModelHubName": "ONNX Model Zoo",
            "MetadataFilePath": "",
            "MetadataObjectID": idx + offset,
        },
        "ModelName": model["Model"]["content"]
        if "content" in model["Model"]
        else model["Model"],
        "ModelURL": url,
    }

    return gen_metadata


def create_specific_metadata(model):
    keys = model.keys() - set(["Model", "path_in_repo"])

    specific_metadata = {}
    for key in keys:
        if model[key] is None:
            continue
        if "Download" == key:
            specific_metadata["size"] = model[key]["content"]
        elif "Download (with sample test data)" == key:
            joined_path = "/".join(model["path_in_repo"].split("/")[2:-1])
            target = model[key]["target"]
            url = f"https://github.com/onnx/models/blob/main/{joined_path}/{target}"
            specific_metadata["ModelURL w/ sample data"] = url
            specific_metadata["size w/ sample data"] = model[key]["content"]
        else:
            specific_metadata[key] = model[key]
    return specific_metadata


# Creates csv for manual parsing
def create_manual_csv(tables_manual):
    for table_manual in map(lambda x: x["path"], tables_manual):
        print(f"Please manually copy {table_manual} into metadata.")

    manual_cols = set()
    for table in tables_manual:
        manual_cols = manual_cols | set(table["header"])
    print(
        f"Create a csv with columns: {manual_cols} and manually parse the above tables into them."
    )

    if "Download" in manual_cols:
        manual_cols |= {"size"}
    if "Download (with sample test data)" in manual_cols:
        manual_cols |= {"size w/ sample data"}
    manual_cols |= {"path_in_repo"}
    manual_cols = manual_cols - set([" (%)"])

    with open("manual_meta.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=manual_cols)
        writer.writeheader()
        for table in tables_manual:
            row = dict.fromkeys(manual_cols)
            row["path_in_repo"] = table["path"]
            writer.writerow(row)
    return manual_cols


def parse_metadata_manual():
    num_metadata_already = max(
        len(glob.glob("./general_metadata/*.json")),
        len(glob.glob("./onnx_metadata/*.json")),
    )
    with open("./manual_meta.csv", "r") as f:
        reader = csv.DictReader(
            f,
        )
        models = []
        for model in reader:
            models.append(model)

    for idx, model in enumerate(models):
        create_metadata(idx, model, offset=num_metadata_already, manual=True)


def create_general_metadata_manual(idx, model, offset):
    url = model["Download"]

    gen_metadata = {
        "id": idx + offset,
        "ModelHub": {
            "ModelHubName": "ONNX Model Zoo",
            "MetadataFilePath": "",
            "MetadataObjectID": idx + offset,
        },
        "ModelName": model["Model"],
        "ModelURL": url,
    }

    return gen_metadata


def create_specific_metadata_manual(model):
    keys = model.keys() - set(["Model", "path_in_repo", "Download"])

    specific_metadata = {}
    for key in keys:
        if model[key] == "":
            continue
        else:
            specific_metadata[key] = model[key]
    return specific_metadata


def parse_metadata():
    readme_paths = glob.glob("./models/**/README.md", recursive=True)

    # Search all README files and find the tables in the file.
    parsed_file_list = []
    for path in readme_paths:
        with open(path, "r") as f:
            with ASTRenderer() as renderer:
                doc = mistletoe.Document(f)
                rendered = renderer.render(doc)
        file_as_json = json.loads(rendered)
        print(f"Searching {path}")
        tables = dfs_table_find(file_as_json)
        parsed_file = {"path": path, "file_as_json": file_as_json, "tables": tables}
        parsed_file_list.append(parsed_file)

    # Filter for all files with tables
    files_w_tables = filter(lambda x: len(x["tables"]) > 0, parsed_file_list)
    files_w_tables = list(files_w_tables)

    # parse tables and save them along with the path of the file they are parsed from.
    parsed_file_tables = []
    for file in files_w_tables:
        parsed_tables = []
        for table in file["tables"]:
            header = dfs_table_parse(table["header"])
            rows = dfs_table_parse(table)
            parsed_table = {"header": header, "rows": rows}
            parsed_tables.append(parsed_table)
        parsed_file_tables.append(
            {"path": file["path"], "parsed_tables": parsed_tables}
        )

    # Write file for any debugging
    with open("parsed_file_tables.json", "w") as f:
        f.write(json.dumps(parsed_file_tables))

    # Parse the rows and headers in the individual files
    all_tables = []
    for p_table in parsed_file_tables:
        path = p_table["path"]
        for table in p_table["parsed_tables"]:
            header = dfs_row_parse(table["header"][0], True)
            rows = list(map(lambda x: dfs_row_parse(x), table["rows"]))
        all_tables.append({"path": path, "header": header, "rows": rows})

    # We need to manually handle tables that whose header size does not equal the number of cells in a row.
    # For all tables that do not have this condition we can parse the table modelwise.
    tables_modelwise = []
    tables_manual = []
    # For debugging purposes
    # tables_that_worked = []
    for table in all_tables:
        path = table["path"]
        if any([len(table["header"]) != len(row) for row in table["rows"]]):
            tables_manual.append(table)
            continue
        for row in table["rows"]:
            table_modelwise = {key: val for key, val in zip(table["header"], row)}
            table_modelwise["path_in_repo"] = path
            tables_modelwise.append(table_modelwise)
        # For debugging purposes
        # tables_that_worked.append(table)

    # Create csv for manual parsing
    manual_cols = create_manual_csv(tables_manual)

    # For the onnx specific metadata we need to know all the keys
    all_keys = {}
    for table in tables_modelwise:
        all_keys = all_keys | table.keys()

    # Use this to build the onnx specific schema
    # with open("./onnx_schema.json", "w") as f:
    #     keys = (
    #         all_keys
    #         | manual_cols
    #         | set(["size", "ModelURL w/ sample data", "size w/ sample data"])
    #     ) - set(
    #         ["Model", "path_in_repo", "Download", "Download (with sample test data)", " (%)"]
    #     )
    #     f.write(json.dumps(dict.fromkeys(keys)))

    # Represent models as dictionary with all keys (many will be none but this makes writing easier)
    models_to_export = []
    for model in tables_modelwise:
        model_w_all_cols = dict.fromkeys(all_keys)
        for key, val in model.items():
            model_w_all_cols[key] = val
        models_to_export.append(model_w_all_cols)

    for i, model in enumerate(models_to_export):
        create_metadata(i, model, 2000)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="onnx-metadata-parser",
        description="This program parses the metadata either automatically (from the onnx model zoo github) or manually from a csv named 'manual_meta.csv'.",
    )
    parser.add_argument(
        "--manual",
        action="store_true",
        default=False,
        help="Set this flag to true to parse metadata from csv. There must be a csv named 'manual_meta.csv' in the current directory",
    )
    args = parser.parse_args()
    if not args.manual:
        parse_metadata()
    else:
        parse_metadata_manual()
