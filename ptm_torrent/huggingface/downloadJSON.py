from typing import List

from huggingface_hub.hf_api import ModelInfo, list_models
from progress.bar import Bar

import ptm_torrent.huggingface as hf
from ptm_torrent.utils.fileSystem import saveJSON
from ptm_torrent.utils.network import downloadJSON


def getModelList() -> List[dict]:
    modelList: List[dict] = []

    print("Getting all PTMs hosted on Hugging Face...")
    resp: List[ModelInfo] = list_models(full=True, cardData=True, fetch_config=True)

    with Bar("Converting response to JSON...", max=len(resp)) as bar:
        model: ModelInfo
        for model in list(iter(resp)):
            modelDict: dict = model.__dict__
            modelDict["siblings"] = [file.__dict__ for file in modelDict["siblings"]]
            modelList.append(modelDict)
            bar.next()
    return modelList


def main() -> None:

    json: List[dict] = getModelList()

    print(f"Saving JSON to {hf.huggingface_HubMetadataPath}")
    saveJSON(json, filepath=hf.huggingface_HubMetadataPath)


if __name__ == "__main__":
    main()
