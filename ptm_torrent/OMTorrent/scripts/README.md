# OMTorrent

## About

This directory contains the code to create the OMTorrent dataset.

This dataset contains three folders:

- `onnx-model-zoo`: a bare repository of the ONNX model zoo
- `general_metadata`: this folder contains individual json files that contain
  "general" metadata (i.e., metadata meeting the schema.json format) about the
  the models in the ONNX model zoo.
- `onnx_metadata`: his folder contains individual json files that contain onnx
  specific metadata (i.e., metadata meeting the onnx_schema.json format) about
  the the models in the ONNX model zoo.

## How to Run

To automatically build the bare repo and the metadata files run the following:

```
cd OMTorrent/scripts
./run.bash
```

If there are README files that need to be parsed manually this script will
output the names of those files and create a csv file with the name
`manual_meta.csv` in `OMTorrent/scripts`. Fill the rows of this file with the
metadata extracted from the tables and then run `handle_manual.sh` (you may need
to add more rows).

To clean up (i.e., remove the models, onnx_metadata, and general_metadata
folders) run `clean_up.sh`.
