#!/bin/bash

# 4_callAPIs.bash
# Call the models, dataset, spaces, and metrics GET APIs to return a list of all
# of the availible repos per category hosted on Hugging Face.
#
# This also creates a .txt file of all the organizations and users on Hugging Face

# Dependencies
# wget
# jq

timestamp=$(date +%s)

./env/bin/python 3a_getModelMetadata.py -t $timestamp
