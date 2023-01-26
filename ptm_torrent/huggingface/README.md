# Hugging Face Torrent

> Scripts to create the Hugging Face component of the greater PTM-Torrent
> dataset

## Table of Contents

- [Hugging Face Torrent](#hugging-face-torrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [Through `__main__.py`](#through-__main__py)
    - [As Individual Files](#as-individual-files)
  - [Data Representation](#data-representation)
    - [Data Directory Specifics](#data-directory-specifics)
      - [`data/huggingface/html`](#datahuggingfacehtml)
      - [`data/huggingface/json`](#datahuggingfacejson)
      - [`data/huggingface/json/metadata`](#datahuggingfacejsonmetadata)
      - [`data/huggingface/repos`](#datahuggingfacerepos)
  - [References](#references)

## About

This directory contains the scripts to download PTM repositories and extract
metadata for the greater *PTMTorrent* dataset from
[Hugging Face](https://huggingface.co).

[Hugging Face](https://huggingface.co) is currently the largest source of PTM
repositories, boasting over 120,000 at the time of release. With that said, the
data storage required to download such a large model hub is non-trivial. Using
the [HFTorrent v1](https://zenodo.org/record/7556031), it took 51TB to download
all roughly 55,000 complete repositories within that dataset.

To accomodate this, we utilize a *shrinkage* parameter within this directory
[`__main__.py`](__main__.py) to only download a subset of the data. This
parameter sets the percentage of models to download from
[Hugging Face](https://huggingface.co) sorted by download in descending order.

Therefore, the scripts within this repository first get a list of all PTM
repositories hosted on [Hugging Face](https://huggingface.co), then sorts the
list by the repository downloads in descending order (e.g. index 0 is the most
downloaded model, index 1 is the second most downloaded model, etc.), and
finally downloads only the top `n%` of models determined by the *shrinkage*
parameter.

To adjust this parameter, please change it within the
[`__main__.py`](__main__.py) file. By default, it is set to 0.1 (10%), which
downloads ~12,000 repositories from [Hugging Face](https://huggingface.co).

## How to Run

To run the scripts within this directory, the larger `ptm_torrent` project and
its dependencies must first be installed. See this project's root
[`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

> If you want to download more or less of a percentage of models from
> [Hugging Face](https://huggingface.co), create an environment variable called
> `HF_TORRENT_SHRINKAGE` and set it to a `float` between 0 and 1 inclusive. By
> default it uses a value of `0.1`.

**You must create a directory called** `split_urls` **in this directory.**

- `python __main__.py`
- `python downloadRepos.py ./split_urls/split_url_<FILE_NUMBER>.txt` (Repeat this for all files in `./split_urls`.)


Or by setting the `HF_TORRENT_SHRINKAGE` value:

- `HF_TORRENT_SHRINKAGE=0.2 python __main__.py`
- `python downloadRepos.py ./split_urls/split_url_<FILE_NUMBER>.txt` (Repeat this for all files in `./split_urls`.)


### As Individual Files

> This method assumes that you accept all of the default values of the scripts.
> Changes can be made manually within the scripts if the defualts are not
> acceptable for your use case.

1. `python setupFileSystem.py`
1. `python downloadJSON.py`
1. `python splitRepos.py`
1. `python downloadRepos.py ./split_urls/split_url_<FILE_NUMBER>.txt` (Repeat this for all files in `./split_urls`.)
1. `python createSchema.py`

## Data Representation

> The following directory structure was taken on 1/25/2023.

```shell
📦data
 ┗ 📂huggingface
 ┃ ┣ 📂html
 ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┗ 📂models
 ┃ ┣ 📂json
 ┃ ┃ ┣ 📜huggingface.json
 ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┗ 📜hf_metadata.json
 ┃ ┃ ┗ 📂repos
 ┃ ┃ ┃ ┗ 📂AUTHOR
 ┃ ┃ ┃ ┃ ┗ 📂MODEL
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

#### `data/huggingface/html`

This directory is not currently utilized by our scripts. It is kept within the
program for consistency across model hubs.

#### `data/huggingface/json`

This directory contains JSON files formatted to fit specific schemas.

The top level file (`huggingface.json`) is formatted to work with the general
[PTMTorrent JSON Schema](../utils/schemas/onnxmodelhubModelMetadata.json).

#### `data/huggingface/json/metadata`

This directory contains JSON files formatted to fit specific schemas.

The file (`hf_metadata.json`) is formatted to work with the
[Model Zoo hub metadata JSON Schema](../utils/schemas/huggingfaceMetadata.json).

#### `data/huggingface/repos`

This directory contains the repository downloaded from the model hub.

Repositories are downloaded into this directory in the format `AUTHOR/REPO`.

Repositories paths are generated by taking the `git` compatible cloning URL and
parsing it for the model *author* and *owner*

> Example: <https://github.com/SoftwareSystemsLaboratory/PTM-Torrent> ->
> SoftwareSystemsLaboratory/PTM-Torrent

## References

> References are sorted by alphabetical order and not how they appear in this
> document.

\[1\] W. Jiang et al., “HFTorrent Dataset.” Zenodo, Jan. 20, 2023. doi:
10.5281/zenodo.7556031.

\[2\] “Hugging Face – The AI community building the future.,” Jan. 03, 2023.
https://huggingface.co/ (accessed Jan. 25, 2023).
