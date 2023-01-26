# Pytorch Hub Torrent

> Scripts to create the Pytorch Hub component of the greater PTM-Torrent dataset

## Table of Contents

- [Pytorch Hub Torrent](#pytorch-hub-torrent)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run](#how-to-run)
    - [Through `__main__.py`](#through-__main__py)
    - [As Individual Files](#as-individual-files)
  - [Data Representation](#data-representation)
    - [Data Directory Specifics](#data-directory-specifics)
      - [`data/pytorchhub/html/metadata`](#datapytorchhubhtmlmetadata)
      - [`data/pytorchhub/json`](#datapytorchhubjson)
      - [`data/pytorchhub/json/metadata`](#datapytorchhubjsonmetadata)
      - [`data/pytorchhub/repos`](#datapytorchhubrepos)
  - [References](#references)

## About

This directory contains the scripts to download PTM repositories and extract
metadata for the greater *PTMTorrent* dataset from
[Pytorch Hub](https://pytorch.org/hub/).

## How to Run

To run the scripts within this directory, the larger `ptm_torrent` project and
its dependencies must first be installed. See this project's root
[`README.md`](../../README.md) for more information.

### Through [`__main__.py`](__main__.py)

- `python __main__.py`

### As Individual Files

> This method assumes that you accept all of the default values of the scripts.
> Changes can be made manually within the scripts if the defualts are not
> acceptable for your use case.

1. `python setupFileSystem.py`
1. `python downloadModelList.py`
1. `python parseModelMetadata.py`
1. `python downloadRepos.py`

## Data Representation

> The following directory structure was taken on 1/25/2023.

```shell
📦data
 ┗ 📂pytorchhub
 ┃ ┣ 📂html
 ┃ ┃ ┗ 📂metadata
 ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┃ ┣ 📜datvuthanh_hybridnets.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_WSL-Images_resnext.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_pytorch-gan-zoo_dcgan.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_pytorch-gan-zoo_pgan.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_pytorchvideo_resnet.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_pytorchvideo_slowfast.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_pytorchvideo_x3d.html
 ┃ ┃ ┃ ┃ ┣ 📜facebookresearch_semi-supervised-ImageNet1K-models_resnext.html
 ┃ ┃ ┃ ┃ ┣ 📜huggingface_pytorch-transformers.html
 ┃ ┃ ┃ ┃ ┣ 📜hustvl_yolop.html
 ┃ ┃ ┃ ┃ ┣ 📜intelisl_midas_v2.html
 ┃ ┃ ┃ ┃ ┣ 📜mateuszbuda_brain-segmentation-pytorch_unet.html
 ┃ ┃ ┃ ┃ ┣ 📜nicolalandro_ntsnet-cub200_ntsnet.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_efficientnet.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_gpunet.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_resnet50.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_resnext.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_se-resnext.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_ssd.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_tacotron2.html
 ┃ ┃ ┃ ┃ ┣ 📜nvidia_deeplearningexamples_waveglow.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_fairseq_roberta.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_fairseq_translation.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_alexnet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_deeplabv3_resnet101.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_densenet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_fcn_resnet101.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_ghostnet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_googlenet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_hardnet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_ibnnet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_inception_v3.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_meal_v2.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_mobilenet_v2.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_once_for_all.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_proxylessnas.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_resnest.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_resnet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_resnext.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_shufflenet_v2.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_snnmlp.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_squeezenet.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_vgg.html
 ┃ ┃ ┃ ┃ ┣ 📜pytorch_vision_wide_resnet.html
 ┃ ┃ ┃ ┃ ┣ 📜sigsep_open-unmix-pytorch_umx.html
 ┃ ┃ ┃ ┃ ┣ 📜snakers4_silero-models_stt.html
 ┃ ┃ ┃ ┃ ┣ 📜snakers4_silero-models_tts.html
 ┃ ┃ ┃ ┃ ┣ 📜snakers4_silero-vad_vad.html
 ┃ ┃ ┃ ┃ ┗ 📜ultralytics_yolov5.html
 ┃ ┃ ┃ ┗ 📜pyth_metadata.html
 ┃ ┣ 📂json
 ┃ ┃ ┣ 📂metadata
 ┃ ┃ ┃ ┣ 📂models
 ┃ ┃ ┃ ┗ 📜pyth_models_metadata.json
 ┃ ┃ ┗ 📜pytorchhub.json
 ┃ ┗ 📂repos
```

> This directory structure is generated relative to where the script is ran
> from. Example: if the script was ran from the home directory (`~`), then the
> `data` directory would be stored at `~/data`.

Where:

- data/MODELHUB/repos/`AUTHOR` is the author name of the repository that was
  cloned.
- data/MODELHUB/repos/AUTHOR/`MODEL` is the name of the repository that was
  cloned.

Model hub scripts do not overwrite the directory. In other words, it is a safe
operation to run multiple model hub scripts from the same directory sequentially
or concurrently.

### Data Directory Specifics

#### `data/pytorchhub/html/metadata`

This directory contains HTML files created from translating Markdown files to
HTML.

The top level file (`pyth_metadata.html`) is the root of the PyTorch Hub.

The sub-directory `models` (`data/pytorchhub/html/metadata/models`) contains the
model cards of specific models within the model zoo in HTML format.

#### `data/pytorchhub/json`

This directory contains JSON files formatted to fit specific schemas.

The top level file (`pytorchhub.json`) is formatted to work with the general
[PTMTorrent JSON Schema](../utils/schemas/onnxmodelhubModelMetadata.json).

#### `data/pytorchhub/json/metadata`

This directory contains JSON files formatted to fit specific schemas.

The file (`pyth_model_metadata.json`) is formatted to work with the
[Pytorch Hub model metadata JSON Schema](../utils/schemas/pytorchhubModelMetadata.json).

#### `data/pytorchhub/repos`

This directory contains the repository downloaded from the model hub.

Repositories are downloaded into this directory in the format `AUTHOR/REPO`.

Repositories paths are generated by taking the `git` compatible cloning URL and
parsing it for the model *author* and *owner*

> Example: <https://github.com/SoftwareSystemsLaboratory/PTM-Torrent> ->
> SoftwareSystemsLaboratory/PTM-Torrent

## References

> References are sorted by alphabetical order and not how they appear in this
> document.

\[1\] “PyTorch Hub.” <https://www.pytorch.org/hub> (accessed Jan. 25, 2023).
