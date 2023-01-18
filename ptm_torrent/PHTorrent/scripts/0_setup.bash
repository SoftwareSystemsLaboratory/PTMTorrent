#!/bin/bash

# 0_setup.bash
# Author: Taylor R. Schorlemmer
# Creates a virtual environment for execution
# Creates folders for intermediate and final files later on.

echo "Creating virtual environment..."
python3 -m venv env

./env/bin/python -m pip install --upgrade pip
./env/bin/python -m pip install -r requirements.txt


echo "Creating directories..."
mkdir ../{html,json,repos}
mkdir ../html/modelPages
