import argparse
import sys
import tomli


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str)
    parser.add_argument("target_str", type=str)
    parser.add_argument("new_str", type=str)
    return parser.parse_args()


def main(file_path: str, target_str: str, replace_str: str):
    with open(file_path, mode="rb") as f:
        buffer: bytes = f.read()
        strs = buffer.decode("utf-8").replace(target_str, replace_str)
        print(strs)


if __name__ == "__main__":
    args = parse_args()
    main(**{k: v for k, v in args._get_kwargs()})
