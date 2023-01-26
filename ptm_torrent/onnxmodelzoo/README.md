# ONNX Model Zoo Torrent

> Scripts to create the ONNX Model Zoo component of the greater PTM-Torrent
> dataset

## Table of Contents

- [ONNX Model Zoo Torrent](#onnx-model-zoo-torrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [Through `__main__.py`](#through-__main__py)
    - [As Individual Files](#as-individual-files)
  - [Data Representation](#data-representation)
    - [Data Directory Specifics](#data-directory-specifics)
      - [`data/onnxmodelhub/html/metadata`](#dataonnxmodelhubhtmlmetadata)
      - [`data/onnxmodelhub/json`](#dataonnxmodelhubjson)
      - [`data/onnxmodelhub/json/metadata`](#dataonnxmodelhubjsonmetadata)
      - [`data/onnxmodelhub/repos`](#dataonnxmodelhubrepos)
  - [References](#references)

## About

This directory contains the scripts to download PTM repositories and extract
metadata for the greater *PTMTorrent* dataset from
[ONNX Model Zoo](https://github.com/onnx/models.co).

## How to Run

To run the scripts within this directory, the larger `ptm_torrent` project and
its dependencies must first be installed. See this project's root
[`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

- `python __main__.py`

### As Individual Files

> This method assumes that you accept all of the default values of the scripts.
> Changes can be made manually within the scripts if the defualts are not
> acceptable for your use case.

1. `python setupFileSystem.py`
1. `python downloadRepos.py`
1. `python mdToHTML.py`
1. `python parseHubHTML.py`
1. `python parseModelHTML.py`

## Data Representation

> The following directory structure was taken on 1/25/2023.

```shell
📦data
 ┗ 📂onnxmodelzoo
 ┃ ┣ 📂html
 ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┣ 📜README_age_gender.html
 ┃ ┃ ┃ ┃ ┣ 📜README_alexnet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_arcface.html
 ┃ ┃ ┃ ┃ ┣ 📜README_bert-squad.html
 ┃ ┃ ┃ ┃ ┣ 📜README_bidirectional_attention_flow.html
 ┃ ┃ ┃ ┃ ┣ 📜README_caffenet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_densenet-121.html
 ┃ ┃ ┃ ┃ ┣ 📜README_duc.html
 ┃ ┃ ┃ ┃ ┣ 📜README_efficientnet-lite4.html
 ┃ ┃ ┃ ┃ ┣ 📜README_emotion_ferplus.html
 ┃ ┃ ┃ ┃ ┣ 📜README_fast_neural_style.html
 ┃ ┃ ┃ ┃ ┣ 📜README_faster-rcnn.html
 ┃ ┃ ┃ ┃ ┣ 📜README_fcn.html
 ┃ ┃ ┃ ┃ ┣ 📜README_googlenet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_gpt-2.html
 ┃ ┃ ┃ ┃ ┣ 📜README_gpt2-bs.html
 ┃ ┃ ┃ ┃ ┣ 📜README_inception_v1.html
 ┃ ┃ ┃ ┃ ┣ 📜README_inception_v2.html
 ┃ ┃ ┃ ┃ ┣ 📜README_mask-rcnn.html
 ┃ ┃ ┃ ┃ ┣ 📜README_mnist.html
 ┃ ┃ ┃ ┃ ┣ 📜README_mobilenet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_rcnn_ilsvrc13.html
 ┃ ┃ ┃ ┃ ┣ 📜README_resnet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_retinanet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_roberta.html
 ┃ ┃ ┃ ┃ ┣ 📜README_shufflenet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_squeezenet.html
 ┃ ┃ ┃ ┃ ┣ 📜README_ssd-mobilenetv1.html
 ┃ ┃ ┃ ┃ ┣ 📜README_ssd.html
 ┃ ┃ ┃ ┃ ┣ 📜README_sub_pixel_cnn_2016.html
 ┃ ┃ ┃ ┃ ┣ 📜README_t5.html
 ┃ ┃ ┃ ┃ ┣ 📜README_tiny-yolov2.html
 ┃ ┃ ┃ ┃ ┣ 📜README_tiny-yolov3.html
 ┃ ┃ ┃ ┃ ┣ 📜README_ultraface.html
 ┃ ┃ ┃ ┃ ┣ 📜README_vgg.html
 ┃ ┃ ┃ ┃ ┣ 📜README_yolov2-coco.html
 ┃ ┃ ┃ ┃ ┣ 📜README_yolov3.html
 ┃ ┃ ┃ ┃ ┣ 📜README_yolov4.html
 ┃ ┃ ┃ ┃ ┗ 📜README_zfnet-512.html
 ┃ ┃ ┃ ┗ 📜README_models.html
 ┃ ┣ 📂json
 ┃ ┃ ┣ 📂metadata
 ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┣ 📜omz_metadata.json
 ┃ ┃ ┃ ┗ 📜omz_models_metadata.json
 ┃ ┃ ┗ 📜onnxmodelzoo.json
 ┃ ┗ 📂repos
 ┃ ┃ ┗ 📂AUTHOR
 ┃ ┃ ┃ ┗ 📂MODEL
```

> This directory structure is generated relative to where the script is ran
> from. Example: if the script was ran from the home directory (`~`), then the
> `data` directory would be stored at `~/data`.

Where:

- data/MODELHUB/repos/`AUTHOR` is the author name of the repository that was
  cloned.
- data/MODELHUB/repos/AUTHOR/`MODEL` is the name of the repository that was
  cloned.

Model hub scripts do not overwrite the directory. In other words, it is a safe
operation to run multiple model hub scripts from the same directory sequentially
or concurrently.

### Data Directory Specifics

#### `data/onnxmodelhub/html/metadata`

This directory contains HTML files created from translating Markdown files to
HTML.

The top level file (`README_models.html`) is the top level `README.md` file of
the ONNX Model Zoo.

The sub-directory `models` (`data/onnxmodelhub/html/metadata/models`) contains
the README.md files of specific models within the model zoo.

These files are parsed to extract data into the either the
[ONNX Model Hub metadata JSON Schema](../utils/schemas/onnxmodelhubHubMetadata.json)
or the
[ONNX Model Hub model metadata JSON Schema](../utils/schemas/onnxmodelhubModelMetadata.json).

#### `data/onnxmodelhub/json`

This directory contains JSON files formatted to fit specific schemas.

The top level file (`onnxmodelzoo.json`) is formatted to work with the general
[PTMTorrent JSON Schema](../utils/schemas/onnxmodelhubModelMetadata.json).

#### `data/onnxmodelhub/json/metadata`

This directory contains JSON files formatted to fit specific schemas.

The file (`omz_metadata.json`) is formatted to work with the
[ONNX Model Hub metadata JSON Schema](../utils/schemas/onnxmodelhubHubMetadata.json).

The file (`omz_model_metadata.json`) is formatted to work with the
[ONNX Model Hub model metadata JSON Schema](../utils/schemas/onnxmodelhubModelMetadata.json).

#### `data/onnxmodelhub/repos`

This directory contains the repository downloaded from the model hub.

Repositories are downloaded into this directory in the format `AUTHOR/REPO`.

Repositories paths are generated by taking the `git` compatible cloning URL and
parsing it for the model *author* and *owner*

> Example: <https://github.com/SoftwareSystemsLaboratory/PTM-Torrent> ->
> SoftwareSystemsLaboratory/PTM-Torrent

## References

> References are sorted by alphabetical order and not how they appear in this
> document.

\[1\] “ONNX Model Zoo.” Open Neural Network Exchange, Jan. 25, 2023. Accessed:
Jan. 25, 2023. \[Online\]. Available: <https://github.com/onnx/models>
