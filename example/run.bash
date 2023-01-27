#!/bin/bash

python3.10 example.py | xargs -I % clime-git-commits-extract -d % &&
clime-git-commits-graph --x-label Days --y-label "Lines of Code" --title "ONNX Model Zoo Lines of Code per Day"
