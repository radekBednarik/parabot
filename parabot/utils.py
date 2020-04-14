import argparse
from datetime import datetime as dt
from pathlib import Path, PurePath
from typing import Any, List


def parse_args() -> Any:
    """Parsers arguments provided by user via CLI.
    
    Returns:
        Any -- object with parsed arguments as attributes
    
    See:
        https://docs.python.org/3/library/argparse.html
    """
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
    parser.add_argument(
        "-t",
        "--tags",
        action="extend",
        nargs="+",
        type=str,
        help="Enter tags of tests/suites you want to run in parallel.",
    )
    return parser.parse_args()


def get_parent_dir(test_filepath: Any) -> Any:
    """Returns PurePath to parent directory of argument filepath.
    
    Arguments:
        test_filepath {Any} -- python Path to .robot file
    
    Returns:
        Any -- python PurePath to parent directory.
    
    See:
        https://docs.python.org/3/library/pathlib.html
    """
    return PurePath(test_filepath).parent


def create_output_folder(basepath: Any, filename: str) -> Any:
    """Returns PurePath to new folder for report of <filename> provided as argument.

    Actual creation of the directory is handled by RobotFramework.
    
    Arguments:
        basepath {Any} -- PurePath to .robot file parent directory
        filename {str} -- .robot file filename
    
    Returns:
        Any -- PurePath to report folder of <filename> .robot file
    """
    timestamp: str = dt.now().strftime("%Y%m%d_%H%M%S")
    dirname: str = "_".join(["report", filename.rstrip(".robot"), timestamp])
    return PurePath(basepath, dirname)


def get_all_robot_files() -> List[Any]:
    """Returns list of Paths of all .robot files in the directory tree.
    
    Returns:
        List[Any] -- Paths of all .robot files in the directory tree.
    """
    return list(Path(".").rglob("*.robot"))


def get_specific_robot_files_by_paths(reldirpaths: List[str]) -> List[Any]:
    """Returns list of Paths of all .robot files in provided list of relative paths.
    
    Arguments:
        reldirpaths {List[str]} -- list of relative paths to .robot files
    
    Returns:
        List[Any] -- Paths to .robot files
    """
    output: List[Any] = []
    for path in reldirpaths:
        [output.append(path_) for path_ in list(Path(path).rglob("*.robot"))]
    return output
