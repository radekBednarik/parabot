import argparse
from datetime import datetime as dt
from pathlib import Path, PurePath
from typing import Any, List


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


def get_parent_dir(test_filepath: Any) -> Any:
    return PurePath(test_filepath).parent


def create_output_folder(basepath: Any, filename: str) -> Any:
    timestamp: str = dt.now().strftime("%Y%m%d_%H%M%S")
    dirname: str = "".join(["report_", filename.rstrip(".robot"), "_", timestamp])
    return PurePath(basepath, dirname)


def get_all_robot_files() -> List[Any]:
    return list(Path(".").rglob("*.robot"))
