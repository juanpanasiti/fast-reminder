import json
import os
from pathlib import Path


def read_json_file(path: str, default_response: list | dict = {}) -> dict:
    os.makedirs(str(Path(path).parent), exist_ok=True)
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        write_json_file(path, default_response)
        return default_response


def write_json_file(path: str, content: dict) -> None:
    with open(path, 'w') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)

