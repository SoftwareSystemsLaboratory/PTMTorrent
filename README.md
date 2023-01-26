# PTMTorrent

> Code to generate the PTMTorrent dataset

[![Python Version](https://img.shields.io/badge/Python-3.10.9-blue)](https://img.shields.io/badge/Python-3.10.9-blue)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7570357.svg)](https://doi.org/10.5281/zenodo.7570357)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/PTM-Torrent/actions/workflows/release.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/PTM-Torrent/actions/workflows/release.yml)

## Table of Contents

- [PTMTorrent](#ptmtorrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Supported Model Hubs](#supported-model-hubs)
  - [Dependencies](#dependencies)
  - [How To Install](#how-to-install)
    - [From GitHub Releases](#from-github-releases)
    - [From Source](#from-source)
  - [How to Run](#how-to-run)
    - [As Individual Scripts](#as-individual-scripts)
  - [Data Representation](#data-representation)
  - [Pre-Packaged Dataset](#pre-packaged-dataset)
  - [Example Usage of Dataset](#example-usage-of-dataset)
  - [How to Cite](#how-to-cite)
  - [References](#references)

## About

This repository contains the scripts to generate the *PTMTorrent* dataset. The
dataset contains sets of pre-trained machine learning models (PTM)
[`git`](https://git-scm.com) repositories hosted on popular model hubs.
Supporting metadata from each model hub as well as standardized metadata
specified by [this JSON Schema](ptm_torrent/utils/schemas/ptmtorrent.json) is
also included in.

### Supported Model Hubs

The following model hubs are supported by our software:

- [Hugging Face](https://huggingface.co/)
- [Modelhub](https://modelhub.ai/)
- [ModelZoo](https://modelzoo.co/)
- [PyTorch Hub](https://pytorch.org/hub/)
- [ONNX Model Zoo](https://github.com/onnx/models/)

## Dependencies

This project is dependent upon the following software:

- [`Python 3.10.9`](https://www.python.org/downloads/release/python-3109/)

> Package dependencies are given in [`pypoetry.toml`](pyproject.toml) and
> handled by [`poetry`](https://python-poetry.org/)

- [`Git`](https://git-scm.com)
- [`Git LFS`](https://git-lfs.com/)

## How To Install

To run this project, it must be packaged and installed first.

The package can either be installed from our
[GitHub Releases](#from-github-releases) or built and installed
[From Source](#from-source).

### From GitHub Releases

1. Download the latest `.tar.gz` or `.whl` file from
   [here](https://github.com/SoftwareSystemsLaboratory/PTM-Torrent/releases).
1. Install via pip: `python3.10 -m pip install ptm_torrent-*`

### From Source

> Instructions were written for Linux operating systems

1. Clone the project locally:
   `git clone https://github.com/SoftwareSystemsLaboratory/PTM-Torrent`
1. `cd` into the project: `cd PTM-Torrent`
1. Create a `Python 3.10` virtual environment: `python3.10 -m venv env`
1. Activate virtual environment: `source env/bin/activate`
1. Upgrade `pip`: `python -m pip install --upgrade pip`
1. Install `poetry`: `python -m pip install poetry`
1. Install `Python` dependencies through `poetry`: `python -m poetry install`
1. Build with `poetry`: `python -m poetry build`
1. Install with `pip`: `python -m pip install dist/ptm_torrent*.tar.gz`

## How to Run

After [installing the package](#how-to-install), this project can be ran as
individual scripts per model hub.

### As Individual Scripts

Each model hub's scripts are separated by directory in the
[`ptm_torrent`](ptm_torrent/) directory. The directory for each specific model
hub's scripts, the main runner script, and download size, is listed in the table
below:

| Model Hub      | Scripts Directory          | Script Name   | Download Size |
| -------------- | -------------------------- | ------------- | ------------- |
| Hugging Face   | `ptm_torrent/huggingface`  | `__main__.py` | 61 TB         |
| Modelhub       | `ptm_torrent/modelhub`     | `__main__.py` | 721 MB        |
| ModelZoo       | `ptm_torrent/modelzoo`     | `__main__.py` | 151 GB        |
| ONNX Model Zoo | `pmt_torrent/onnxmodelzoo` | `__main__.py` | 441 MB        |
| Pytorch Hub    | `ptm_torrent/pytorchhub`   | `__main__.py` | 1.5 GB        |

<!-- Table created with https://www.tablesgenerator.com/markdown_tables -->

There are other supporting scripts within each model hub's scripts directory.
These scripts are ran in order by the model hub's `__main__.py` file. The order
in which to run these scripts (should the `__main__.py` file be insufficient) is
described in each model hub's `README.md` file within the scripts directory.

> NOTE: Hugging Face's `__main__.py` can be parameritized to allow for a
> specific percentage of the model hub to be downloaded. By default, it is the
> first 0.1 (10%) of models sorted by downloads in descending order.

To run any of the scripts, execute the following command pattern:

- `python 'Scripts Directory'/'Script Name'`

For example, to run Hugging Face's scripts:

- `python ptm_torrent/huggingface/__main__.py`

## Data Representation

Each model hub script generates the following directory structure **per model
hub**:

```shell
📦data
 ┗ 📂MODELHUB
 ┃ ┣ 📂html
 ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┃ ┗ 📂models
 ┃ ┃ ┣ 📂json
 ┃ ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┃ ┗ 📂models
 ┃ ┃ ┗ 📂repos
 ┃ ┃ ┃ ┗ 📂AUTHOR
 ┃ ┃ ┃ ┃ ┗ 📂MODEL
```

> This directory structure is generated relative to where the script is ran
> from. Example: if the script was ran from the home directory (`~`), then the
> `data` directory would be stored at `~/data`.

Where:

- data/`MODELHUB` is the same name as the `Python` module directory that
  contained the script.
- data/MODELHUB/repos/`AUTHOR` is the author name of the repository that was
  cloned.
- data/MODELHUB/repos/AUTHOR/`MODEL` is the name of the repository that was
  cloned.

Model hub scripts do not overwrite the directory. In other words, it is a safe
operation to run multiple model hub scripts from the same directory sequentially
or concurrently.

Specifics about the types of metadata files and content that are produced by the
scripts can be found in each model hub's script directory's `README.md` file.

## Pre-Packaged Dataset

An existing dataset is availible on
[this Purdue University Globus share](https://app.globus.org/file-manager?origin_id=55e17a6e-9d8f-11ed-a2a2-8383522b48d9&origin_path=%2F%7E%2F).
It currently is 99.79 GB as compressed `tar.gz` archives.

## Example Usage of Dataset

An example usage of the dataset is described within the
[`example`](example/README.md) directory.

## How to Cite

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7570357.svg)](https://doi.org/10.5281/zenodo.7570357)

This project has a DOI on [Zenodo](https://doi.org/10.5281/zenodo.7570357).
Please visit our Zenodo page for the latest citation information.

## References

> References are sorted by alphabetical order and not how they appear in this
> document.

\[1\] “Git.” <https://git-scm.com/> (accessed Jan. 25, 2023).

\[2\] “Git Large File Storage,” Git Large File Storage. <https://git-lfs.com/>
(accessed Jan. 25, 2023).

\[3\] “Hugging Face – The AI community building the future.,” Jan. 03, 2023.
<https://huggingface.co/> (accessed Jan. 25, 2023).

\[4\] “Model Zoo - Deep learning code and pretrained models for transfer
learning, educational purposes, and more.” <https://modelzoo.co/> (accessed Jan.
25, 2023).

\[5\] “Modelhub.” <https://modelhub.ai/> (accessed Jan. 25, 2023).

\[6\] “MSR 2023 - Data and Tool Showcase Track - MSR 2023.”
<https://conf.researchr.org/track/msr-2023/msr-2023-data-showcase> (accessed
Jan. 25, 2023).

\[7\] “ONNX Model Zoo.” Open Neural Network Exchange, Jan. 25, 2023. Accessed:
Jan. 25, 2023. \[Online\]. Available: <https://github.com/onnx/models>

\[8\] “pip documentation v22.3.1.” <https://pip.pypa.io/en/stable/> (accessed
Jan. 25, 2023).

\[9\] “Poetry - Python dependency management and packaging made easy.”
<https://python-poetry.org/> (accessed Jan. 25, 2023).

\[10\] “Python Release Python 3.10.9,” Python.org.
<https://www.python.org/downloads/release/python-3109/> (accessed Jan. 25,
2023).

\[11\] “PyTorch Hub.” <https://www.pytorch.org/hub> (accessed Jan. 25, 2023).

\[12\] W. Jiang et al., “SoftwareSystemsLaboratory/PTMTorrent.” Zenodo, Jan. 25,
2023\. doi: 10.5281/zenodo.7570357.
