# PHTorrent

PyTorch Hub PTM Torrent Scripts

## About

This directory contains the code to create the PHTorrent dataset. It relies on a
few dependencies listed in `/scripts/requirements.txt`. These should be
automatically downloaded by the Python virtual environment.

The scripts scrape HTML data from https://pytorch.org/hub/ to find GitHub
repository locations and information for the JSON files.

The `/json/general.json` file complies with the `../schema.json` schema and the
`/json/specific.json` file complies with the `PHTorrent.schema.json` schema.

## Use

- Run the `./scripts/run.bash` file to create the torrent.
- Run the `./scripts/nuke.bash` file to delete **ALL** generated files and
  folders.
