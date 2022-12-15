#!/bin/bash

# WARNING: This delets all data that has been created by the scripts in this folder.
# You will have to recreate all of the data after running this script

rm -r ../{html,csv,json,txt}
yes | rm -r env
