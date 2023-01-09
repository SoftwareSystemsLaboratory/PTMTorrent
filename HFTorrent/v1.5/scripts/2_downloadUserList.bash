#!/bin/bash

# 2_downloadUserList.bash
# Download the HTML file containing all pro users on Hugging Face
# The full set of users can be found by taking the set of authors from the
# models, datasets, spaces, and metrics JSON API responses

# Dependencies:
# wget

wget -O ../html/users/proUsers_$(date +%s).html https://huggingface.co/users
