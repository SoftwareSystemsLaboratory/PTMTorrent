# Pytorch Hub Torrent

> Scripts to create the Pytorch Hub component of the greater PTM-Torrent dataset

## Table of Contents

- [Hugging Face Torrent](#hugging-face-torrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [As a Python Package](#as-a-python-package)
    - [As Individual Scripts](#as-individual-scripts)
  - [Data Storage](#data-storage)
    - [From Python Package](#from-python-package)
    - [From Individual Scripts](#from-individual-scripts)
  - [References](#references)

## About

This folder contains the scripts to download PTM repositories and extract metadata for the greater *PTMTorrent* dataset from [Pytorch Hub](https://pytorch.org/hub/).

To download the entirety of the [Pytorch Hub](https://pytorch.org/hub/) model hub requires nGB of storage.

## How to Run

To run the scripts within this folder, the larger `ptm_torrent` project and its dependencies must first be installed.
See this project's root [`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

- `python __main__.py`

### As Individual Files

> This method assumes that you accept all of the default values of the scripts.
> Changes can be made manually within the scripts if the defualts are not acceptable for your use case.

1. `python setupFileSystem.py`
2. `python downloadModelList.py`
3. `python parseModelMetadata.py`
4. `python downloadRepos.py`

## Data Storage

## References
