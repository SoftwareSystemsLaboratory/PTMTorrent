#!/bin/bash

# 4_callAPIs.bash
# Call the models, dataset, spaces, and metrics GET APIs to return a list of all 
# of the availible repos per category hosted on Hugging Face

# Dependencies
# wget

wget -O models.json https://huggingface.co/api/models
wget -O datasets.json https://huggingface.co/api/datasets
wget -O spaces.json https://huggingface.co/api/spaces
wget -O metrics.json https://huggingface.co/api/metrics

