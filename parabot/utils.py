import argparse
from pathlib import Path
from typing import List, Any, Generator


def parse_args() -> Any:
    parser: Any = argparse.ArgumentParser(
        description="What tests do you want to run in parallel?"
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Parallelize execution of all .robot files",
    )
    return parser.parse_args()


def get_all_robot_files() -> List[Any]:
    return list(Path(".").rglob("*.robot"))


if __name__ == "__main__":
    print(get_all_robot_files())
