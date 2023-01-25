# Model Zoo Torrent

> Scripts to create the Model Zoo component of the greater PTM-Torrent dataset

## Table of Contents

- [Model Zoo Torrent](#model-zoo-torrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [Through `__main__.py`](#through-__main__py)
    - [As Individual Files](#as-individual-files)
  - [Data Storage](#data-storage)
  - [References](#references)

## About

This folder contains the scripts to download PTM repositories and extract
metadata for the greater *PTMTorrent* dataset from
[Model Zoo](https://modelzoo.co).

To download the entirety of the [Model Zoo](https://modelzoo.co) model hub
requires nGB of storage.

## How to Run

To run the scripts within this folder, the larger `ptm_torrent` project and its
dependencies must first be installed. See this project's root
[`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

- `python __main__.py`

### As Individual Files

> This method assumes that you accept all of the default values of the scripts.
> Changes can be made manually within the scripts if the defualts are not
> acceptable for your use case.

1. `python setupFileSystem.py`
1. `python downloadHubJSON.py`
1. `python downloadModelJSON.py`
1. `python downloadRepos.py`
1. `python createSchema.py`

## Data Storage

## References

> References are sorted by alphabetical order and not how they appear in this
> document.
