import argparse
import sys
import tomli


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str)
    parser.add_argument("target_str", type=str)
    parser.add_argument("replace_str", type=str)
    return parser.parse_args()


def main(file_path: str, target_str: str, replace_str: str):
    with open(file_path, mode="r") as f:
        buffer: str = f.read()
        strs = buffer.replace(target_str, replace_str)
    with open(file_path, mode="w") as f:
        f.write(strs)


if __name__ == "__main__":
    args = parse_args()
    main(**{k: v for k, v in args._get_kwargs()})
