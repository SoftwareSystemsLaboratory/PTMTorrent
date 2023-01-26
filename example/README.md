# Example Usage of Output Data from PTMTorrent

> This directory contains a script to collect data from a repository from the
> *PTMTorrent* dataset.

## Table of Contents

- [Example Usage of Output Data from PTMTorrent](#example-usage-of-output-data-from-ptmtorrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Dependencies](#dependencies)
  - [How to Run](#how-to-run)
  - [References](#references)

## About

This is an example program that extracts and graphs commit information from
repositories.

This directory contains a `Python 3.10` script that reads and extracts model
paths from an example JSON file (from the
[ONNX Model Zoo component](../ptm_torrent/onnxmodelzoo/README.md)).

This is then passed into
[`PRIME`](https://github.com/SoftwareSystemsLaboratory/PRIME) which extracts
commit related information and plots it.

## Dependencies

This program is dependent upon
[*PTMTorrent* being installed](../README.md#how-to-install), as well
[`PRIME`'s dependencies](https://github.com/SoftwareSystemsLaboratory/PRIME).

## How to Run

> Instructions were written for Linux operating systems

1. Create a `Python 3.10` virtual environment: `python3.10 -m venv env`
1. Activate virtual environment: `source env/bin/activate`
1. Upgrade `pip`: `python -m pip install --upgrade pip`
1. Execute the program with: `./run.bash`

## References

\[1\] N. Synovic and G. K. Thiruvathukal,
“SoftwareSystemsLaboratory/clime-metrics.” Zenodo, Apr. 25, 2022. doi:
10.5281/zenodo.6484082.
