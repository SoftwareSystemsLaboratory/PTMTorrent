#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv env

./env/bin/python -m pip install -U pip
./env/bin/python -m pip install -r requirements.txt
