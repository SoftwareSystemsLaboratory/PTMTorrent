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

wget -O ../json/models_$timestamp.json https://huggingface.co/api/models
# wget -O ../json/datasets_$timestamp.json https://huggingface.co/api/datasets
# wget -O ../json/spaces_$timestamp.json https://huggingface.co/api/spaces
# wget -O ../json/metrics_$timestamp.json https://huggingface.co/api/metrics

jq .[].id ../json/models_$timestamp.json | grep '/' | grep -o ^[^/]* | sed 's/"//g' | sort -f | uniq > ../txt/allUsersOrganizations_$timestamp.txt
jq .[].id ../json/models_$timestamp.json | grep '/' | grep -o ^[^/]* | sed 's/"//g' | sort -f | uniq -c > ../txt/allUsersOrganizationsModelCounts_$timestamp.txt
jq .[].id ../json/models_$timestamp.json | grep '/' |  sed 's/"//g' | sort -f > ../txt/modelIDs_$timestamp.txt
