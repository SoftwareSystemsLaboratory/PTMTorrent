#!/bin/bash

git clone https://github.com/onnx/models onnx/models

# python3.10 example.py | xargs -I % clime-git-commits-extract -d % &&
clime-git-commits-graph
