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
    parser.add_argument(
        "-f",
        "--folders",
        action="extend",
        nargs="+",
        type=str,
        help="Enter relative path to specific folder with .robot files.",
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


def get_specific_robot_files_by_paths(reldirpaths: List[str]) -> List[Any]:
    output: List[Any] = []
    for path in reldirpaths:
        [output.append(path_) for path_ in list(Path(path).rglob("*.robot"))]
    return output
