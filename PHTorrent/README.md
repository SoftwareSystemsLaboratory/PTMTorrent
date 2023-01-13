# PHTorrent
> PyTorch Hub PTM Torrent Scripts

## About
This directory contains the code to create the PHTorrent dataset. It relies on a few dependencies listed in `/scripts/requirements.txt`. These should be automatically downloaded by the Python virtual environment.

The scripts scrape HTML data from https://pytorch.org/hub/ to find GitHub repository locations and information for the JSON files.

## How To Run
Run the `./scripts/run.bash` file to create the torrent.

Run the `./scripts/nuke.bash` file to delete **ALL** generated files and folders.
