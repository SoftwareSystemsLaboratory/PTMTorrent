# Hugging Face Torrent

> Scripts to create the Hugging Face component of the greater PTM-Torrent dataset

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

This folder contains the scripts to download PTM repositories and extract metadata for the greater *PTMTorrent* dataset from [Hugging Face](https://huggingface.co).

[Hugging Face](https://huggingface.co) is currently the largest source of PTM repositories, boasting over 120,000 at the time of release.
With that said, the data storage required to download such a large model hub is non-trivial.
Using the [HFTorrent v1](https://zenodo.org/record/7556031), it took 51TB to download all roughly 55,000 complete repositories within that dataset.

To accomodate this, we utilize a *shrinkage* parameter within this folder [`__main__.py`](__main__.py) to only download a subset of the data.
This parameter sets the percentage of models to download from [Hugging Face](https://huggingface.co) sorted by download in descending order.

Therefore, the scripts within this repository first get a list of all PTM repositories hosted on [Hugging Face](https://huggingface.co), then sorts the list by the repository downloads in descending order (e.g. index 0 is the most downloaded model, index 1 is the second most downloaded model, etc.), and finally downloads only the top `n%` of models determined by the *shrinkage* parameter.

To adjust this parameter, please change it within the [`__main__.py`](__main__.py) file.
By default, it is set to 0.1 (10%), which downloads ~12,000 repositories from [Hugging Face](https://huggingface.co).

## How to Run

To run the scripts within this folder, the larger `ptm_torrent` project and its dependencies must first be installed.
See this project's root [`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

> If you want to download more or less of a percentage of models from [Hugging Face](https://huggingface.co), adjust the *shrinkage* parameter in [`__main__.py`](__main__.py) prior to executing the command.

- `python __main__.py`

### As Individual Files

This method assumes that you accept all of the default values of the scripts.
Changes can be made manually within the scripts if the defualts are not acceptable for your use case.

1. `python setupFileSystem.py`
2. `python downloadJSON.py`
3. `python downloadRepos.py`

## Data Storage

## References
