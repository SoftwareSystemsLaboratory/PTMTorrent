from requests import Response, get

defaultHeaders: dict = {"User-Agent": "PTMTorrent"}


def downloadJSON(
    url: str, headers: dict = defaultHeaders, data: dict = {}
) -> dict | int:
    resp: Response = get(url=url, headers=headers, data=data)

    if resp.status_code != 200:
        return resp.status_code

    return resp.json()


def downloadHTML(url: str, headers: dict = defaultHeaders) -> str | int:
    resp: Response = get(url, headers)

    if resp.status_code != 200:
        return resp.status_code

    return resp.content.decode("UTF-8")
