from json import dumps
from time import time

import pandas
from huggingface_hub import list_models, login
from huggingface_hub.hf_api import ModelInfo, RepoFile
from pandas import DataFrame
from progress.bar import Bar

stor: DataFrame = DataFrame()

print("Getting a list of models from Hugging Face...")
resp = list_models(full=True, cardData=True, fetch_config=True)
data: list = [model.__dict__ for model in list(iter(resp))]

with Bar("Converting models into a JSON compatible format...", max=len(data)) as bar:
    model: dict
    for model in data:
        model["siblings"] = [file.__dict__ for file in model["siblings"]]
        bar.next()

print("Exporting JSON to file...")
df: DataFrame = pandas.read_json(dumps(data)).T
df.to_json("test.json")
