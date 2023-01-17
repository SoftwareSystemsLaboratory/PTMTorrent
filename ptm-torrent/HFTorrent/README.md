# HFTorrent

> Hugging Face PTM Torrent scripts

## About

This directory contains the code to create the HFTorrent dataset.

The HFTorrent dataset contains `git bare` repositories of both PTMs and datasets
hosted on Hugging Face. Additionally, it includes information about the authors
and organizations on Hugging Face.

This utility downloads the HTML pages from Hugging Face to analyze both User and
Organization information that is inaccessible through the Hugging Face REST API.
It does use the REST API to return model information and stores it in JSON.

## How To Run

Run `./scripts/run.bash` to create the torrent.

Run `./scripts/nuke.bash` to delete all collected information **including the
torrent**.
