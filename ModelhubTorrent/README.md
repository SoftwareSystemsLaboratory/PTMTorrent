# MHTorrent

> [Modelhub](http://app.modelhub.ai) PTM Torrent scripts

## About

This directory contains the code to create the MHTorrent dataset.

The MHTorrent dataset contains `git bare` repositories of PTMs hosted on ModelHub.

This utility gets the current state of modelhub collection, which is a single JSON file as of now. It then goes through each github repository and
clones it (bare).

We do not use the modelhub REST api as we can interface with git instead

## How To Run

Run `./scripts/run.bash` to create the torrent.

<!--
TODO
Run `./scripts/nuke.bash` to delete all collected information **including the torrent**. -->
