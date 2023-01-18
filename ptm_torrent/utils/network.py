from json import dump
from pathlib import PurePath

from requests import Response, get


def downloadJSON(url: str, headers: dict = {"User-Agent": "PTMTorrent"}) -> dict | int:
    resp: Response = get(url, headers)

    if resp.status_code != 200:
        return resp.status_code

    return resp.json()
