# parse_config.py
from typing import List
import yaml
import sys


def get_config_value(args: List[str]):
    with open("config.yaml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        for arg in args:
            if arg not in cfg:
                raise KeyError(f"{arg} is NOT in {cfg}")
            cfg = cfg[arg]
        return cfg


if __name__ == "__main__":
    args = sys.argv[1:]
    print(get_config_value(args))
