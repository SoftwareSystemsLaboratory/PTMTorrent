# MHTorrent

> [Modelhub](http://app.modelhub.ai) PTM Torrent scripts

## About

This directory contains the code to create the MHTorrent dataset.

The MHTorrent dataset contains `git bare` repositories of PTMs hosted on
ModelHub.

This utility gets the current state of modelhub collection, which is a single
JSON file as of now. It then goes through each github repository and clones it
(bare).

We do not use the modelhub REST api as we can interface with git instead

## How To Run

Run `./scripts/run.bash` to create the torrent.

the script should take around 20-30 mins to download all the data

## Output format

After executing run.bash, the script will populate the `repo` and the `json`
directories with the bare clones and the required metadata.
![https://imgur.com/TWf5Dfl](https://i.imgur.com/TWf5Dfl.jpg)

Each model will have an individual directory in these folders:

![https://imgur.com/QXypaYL](https://i.imgur.com/QXypaYL.jpg)
![https://imgur.com/BdeHzW2](https://i.imgur.com/BdeHzW2.jpg)
![https://imgur.com/IZOPMzB](https://i.imgur.com/IZOPMzB.jpg)

The full repos are generated from the bare repositories. The script also
downloads any externally hosted model.

In some cases if the model returns a 404 ( only 1 such known issue ), those
models will be skipped.

To clear the generated files and "reset" the script, run `nuke.bash`
