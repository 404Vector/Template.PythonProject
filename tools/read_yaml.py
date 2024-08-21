# parse_config.py
from typing import List
import yaml
import json
import sys


def convert_yaml_to_json(yaml_path):
    with open(yaml_path, "r") as file:
        yaml_content = yaml.safe_load(file)
        json_content = json.dumps(yaml_content)
        return json_content


if __name__ == "__main__":
    path = sys.argv[1]
    print(convert_yaml_to_json(path))
