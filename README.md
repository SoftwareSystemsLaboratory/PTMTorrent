# PTMTorrent

> Code to generate the PTMTorrent dataset

[![Python Version](https://img.shields.io/badge/Python-3.10.9-blue)](https://img.shields.io/badge/Python-3.10.9-blue)
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
  - [Data Storage](#data-storage)
  - [How to Cite](#how-to-cite)
  - [References](#references)

## About

This repository contains the scripts to generate the *PTMTorrent* dataset.

*PTMTorrent* is a dataset created to be submitted to the
[2023 Mining Software Repositories (MSR) Confrence Data and Tool Showcase Track](https://conf.researchr.org/track/msr-2023/msr-2023-data-showcase).
The dataset contains either the partial or entire set of pre-trained machine
learning models (PTM) repositories hosted on popular model hubs.

> Model hubs are, "collections of PTMs and datasets organized by problem domain"
> (from ICSE paper).

The list of currently supported model hubs can be found
[here](#supported-model-hubs).

### Supported Model Hubs

The following model hubs are supported by our software:

- [Hugging Face](https://huggingface.co/)
- [Modelhub](https://modelhub.ai/)
- [ModelZoo](https://modelzoo.co/)
- [Pytorch Hub](https://pytorch.org/hub/)
- [ONNX Model Zoo](https://github.com/onnx/models/)

## Dependencies

This project is dependent upon the following software:

- [`Python 3.10.9`](https://www.python.org/downloads/release/python-3109/)

> Python dependencies and packaging are handled by
> [`pip`](https://pip.pypa.io/en/stable/) and
> [`poetry`](https://python-poetry.org/)

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

> Instructions were written with respect to Linux operating systems

1. Clone the project locally:
   `git clone https://github.com/SoftwareSystemsLaboratory/PTM-Torrent`
1. `cd` into project: `cd PTM-Torrent`
1. Create a `Python 3.10` virtual environment: `python3.10 -m venv env`
1. Activate virtual environment: `source env/bin/activate`
1. Upgrade `pip`: `python -m pip install --upgrade pip`
1. Install `poetry`: `python -m pip install -r requirements.txt`
1. Install `Python` dependencies through `poetry`: `python -m poetry install`
1. Build with `poetry`: `python -m poetry build`
1. Install with `pip`: `python -m pip install dist/ptm_torrent*.tar.gz`

## How to Run

After [installing the package](#how-to-install), this project can be ran as
indvidual scripts per model hub.

### As Individual Scripts

Each model hub's scripts are seperated by folder in the
[`ptm_torrent`](ptm_torrent/) folder. The folder for each specific model hub, as
well as the main runner script, is listed in the table below:

| Model Hub      | Scripts Folder             | Script Name   |
| -------------- | -------------------------- | ------------- |
| Hugging Face   | `ptm_torrent/huggingface`  | `__main__.py` |
| Modelhub       | `ptm_torrent/modelhub`     | `__main__.py` |
| ModelZoo       | `ptm_torrent/modelzoo`     | `__main__.py` |
| Pytorch Hub    | `ptm_torrent/pytorchhub`   | `__main__.py` |
| ONNX Model Zoo | `pmt_torrent/onnxmodelzoo` | `__main__.py` |

<!-- Table created with https://www.tablesgenerator.com/markdown_tables -->

There are other supporting scripts within each model hub's scripts folder. These
scripts are ran in order by the model hub's `__main__.py` file. The order in
which to run these scripts (should the `__main__.py` file be insufficient) is
described in each model hub's `README.md` file within the scripts folder.

> NOTE: Hugging Face's `__main__.py` can be parameritized to allow for a
> specific percentage of the model hub to be downloaded. By default it is 0.1
> (10%).

To run any of the scripts, execute the following command pattern:

- `python 'Scripts Folder'/'Script Name'`

For example, to run Hugging Face's scripts:

- `python ptm_torrent/huggingface/__main__.py`

## Data Storage

Each model hub script generates the following directory structure **per model
hub**:

```shell
📂data
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

> This folder structure is generated relative to where the script is ran from.
> Example: if the script was ran from the home directory (`~`), then the `data`
> folder would be stored at `~/data`.

Where:

- data/`MODELHUB` is the same name as the `Python` module folder that contained
  the script.
- data/MODELHUB/repos/`AUTHOR` is the author name of the repository that was
  cloned.
- data/MODELHUB/repos/AUTHOR/`MODEL` is the name of the repository that was
  cloned.

Specifics about the types of metadata files and content that is produced by the
scripts can be found in each model hub's script folder's `README.md` file.

## How to Cite

## References
