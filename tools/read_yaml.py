# parse_config.py
from typing import List
import yaml
import sys


def get_config_value(path, args: List[str]):
    with open(path, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        for arg in args:
            if arg not in cfg:
                raise KeyError(f"{arg} is NOT in {cfg}")
            cfg = cfg[arg]
        return cfg


if __name__ == "__main__":
    path = sys.argv[1]
    args = sys.argv[2:]
    print(get_config_value(path, args))
