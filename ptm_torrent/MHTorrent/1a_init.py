"""
Initialize by downloading all repos from modelhub.ai
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor
from json import dumps, loads
from os import environ
from pathlib import Path
from typing import Dict, List, Literal

import requests
from model import Model
from model_types import TModelResponse
from util import handle_errors

curr: Path
repos_dir: Path
model_metadat_root: Path
full_repo_dir: Path
bare_repo_dir: Path


MODEL_JSON_URL = (
    "https://raw.githubusercontent.com/modelhub-ai/modelhub/master/models.json"
)

headers = {"User-Agent": "MHTorrent - python/requests"}


def get_overview() -> List[TModelResponse]:
    """
    get the main models.json file from modelhub repo.
    this approach is okay to use as modelhub official repositories
    seem to be using this approach to get the model index
    https://github.com/modelhub-ai/unet-2d/blob/master/init/start.py#L203

    """
    resp = requests.get(MODEL_JSON_URL, headers=headers, timeout=60)
    (json_dir / "models.json").write_bytes(resp.content)
    return resp.json()


def subprocess_run(arg_list):
    """
    wrap subprocess.arg and show the command being executed
    """
    args = list(str(x) for x in arg_list)
    print("$", " ".join(args))
    # pylint: disable=subprocess-run-check
    res = subprocess.run(args, capture_output=True)
    if res.returncode != 0:
        print(res.stderr.decode())
    res.check_returncode()
    return res


def download_file(url: str, dest: Path):
    """
    wrap wget or maybe implement a requests based streaming downlaod
    """
    # strategy = "wget"  # or requests
    # if strategy == "wget":
    args = ["wget", url, "-O", str(dest)]

    print(
        f"download finished for {url}"
        if subprocess_run(args).returncode == 0
        else f"download failed for {url}"
    )


def bare_to_full(model_metadata: TModelResponse, bare_repo_path: Path):
    """
    Convert a bare git repo to a full repo
    """
    full_repo = full_repo_dir / model_metadata["name"]
    remote = model_metadata["github"]

    subprocess_run(["git", "clone", "-l", f"{bare_repo_path}", f"{full_repo}"])
    subprocess_run(["git", "-C", f"{full_repo}", "remote", "set-url", "origin", remote])
    subprocess_run(["git", "-C", f"{full_repo}", "restore", "--source=HEAD", ":/"])


@handle_errors
def clone_repo(model_meta: TModelResponse):
    """Clone repo, make sure name matches the json response"""
    name = model_meta["name"]
    args = [
        "git",
        "clone",
        "--bare",
        model_meta["github"],
        bare_repo_dir / f"{name}.git",
    ]

    # skip cloning repos?
    if not environ.get("MHTORRENT_SKIP_CLONE"):
        subprocess_run(args)
        bare_to_full(model_meta, bare_repo_dir / f"{name}.git")
    repo_root = full_repo_dir / name
    data = loads((repo_root / "init/init.json").read_text())
    if data.get("external_contrib_files"):
        for external_files in data["external_contrib_files"]:
            src: str = external_files["src_url"]
            # some init.json files have completely broken urls (they use them as comments instead)
            # which is not great
            # lucklily their urls start with https:// so we can just check for that
            if not src.startswith("https://"):
                continue
            dest: str = external_files["dest_file_path"]
            # make sure pathlib doesn't end up giving us a `/contrib_src` path
            if dest.startswith("/"):
                dest = dest[1:]
            realpath = repo_root / dest
            if environ.get("MHTORRENT_SKIP_DOWNLOAD"):
                print("skipping download")
            else:
                print(f"downloading {src} to {realpath}")
                try:
                    download_file(src, realpath)
                # pylint: disable=broad-except
                except Exception as _:
                    print(f"Failed to download {src}. Skipping {name}")
    config = loads((repo_root / "contrib_src/model/config.json").read_text())
    model_metadata_dir = safe_dir(model_metadata_root / name)
    mh_metadata_path = model_metadata_dir / "modelhub.json"
    sha = subprocess_run(["git", "-C", repo_root, "rev-parse", "HEAD"]).stdout.decode()
    model = Model(
        config,
        mh_metadata_path.relative_to(model_metadata_dir),
        model_meta["github"],
        sha,
    )
    (model_metadata_dir / "model.json").write_text(dumps(model.as_json))
    mh_metadata_path.write_text(dumps(config))


def safe_dir(where: str):
    """
    like mkdir p
    """
    res = curr / where
    res.mkdir(exist_ok=True)
    return res


def create_model_repos():
    """go through each model and clone the repo"""
    models_file = json_dir / "models.json"

    if environ.get("MHTORRENT_USE_LOCAL_MODEL_INDEX"):
        models = loads(models_file.read_text())
    else:
        models = get_overview()

    # clone the models in a threadpool
    # workers could be configurable but 5 seems to be able to finish the job quickly
    exc = ThreadPoolExecutor(max_workers=5)
    for model_meta in models:
        exc.submit(clone_repo, model_meta)


if __name__ == "__main__":
    curr = Path()
    repos_dir = safe_dir("../repos")
    json_dir = safe_dir("../json")
    full_repo_dir = safe_dir(repos_dir / "full")
    bare_repo_dir = safe_dir(repos_dir / "bare")
    model_metadata_root = safe_dir(json_dir / "models")
    create_model_repos()
