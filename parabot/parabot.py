from multiprocessing import Pool
from typing import Any, Callable, List

from robot.run import run

from parabot.utils import (
    get_all_robot_files,
    parse_args,
    get_parent_dir,
    create_output_folder,
)


def worker(filepath: Any) -> None:
    basepath: Any = get_parent_dir(filepath)
    run(filepath, outputdir=create_output_folder(basepath, filepath.name))


def pool_jobs(worker: Callable, filepathslist: List[Any]) -> None:
    with Pool(maxtasksperchild=1) as p:
        p.map(worker, filepathslist)


def main() -> None:
    args: Any = parse_args()

    if args.all:
        filepathslist: List[Any] = get_all_robot_files()
        pool_jobs(worker, filepathslist)
