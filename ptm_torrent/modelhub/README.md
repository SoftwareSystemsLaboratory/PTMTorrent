# Modelhub Torrent

> Scripts to create the Modelhub component of the greater PTM-Torrent dataset

## Table of Contents

- [Modelhub Torrent](#modelhub-torrent)
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
[Modelhub](https://modelhub.ai).

To download the entirety of the [Modelhub](https://modelhub.ai) model hub
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
1. `python downloadJSON.py`
1. `python downloadRepos.py`
1. `python createSchema.py`

## Data Storage

## References

> References are sorted by alphabetical order and not how they appear in this
> document.

\[1\] “Modelhub.” https://modelhub.ai/ (accessed Jan. 25, 2023).
