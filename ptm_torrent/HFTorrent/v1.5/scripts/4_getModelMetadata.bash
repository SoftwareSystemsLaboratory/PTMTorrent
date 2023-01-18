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

./env/bin/python 4a_getModelMetadata.py -t $timestamp

jq .[].author ../json/models_$timestamp.json | sed 's/"//g' | sort | uniq > ../txt/allAuthors_$timestamp.txt
jq .[].author ../json/models_$timestamp.json | sed 's/"//g' | sort | uniq -c > ../txt/authorModelCountMapping_$timestamp.txt
jq .[].id ../json/models_$timestamp.json | sed 's/"//g' | sort | uniq > ../txt/modelIDs_$timestamp.txt
