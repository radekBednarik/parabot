from multiprocessing import Pool
from subprocess import run
from typing import Any, List, Callable

from robot.run import run

from parabot.utils import parse_args, get_all_robot_files


def worker(filepath: str) -> None:
    run(filepath)


def pool_jobs(worker: Callable, filepathslist: List[Any]) -> None:
    with Pool(maxtasksperchild=1) as p:
        p.map(worker, filepathslist)


def main() -> None:
    args: Any = parse_args()

    if args.all:
        filepathslist: List[Any] = get_all_robot_files()
        pool_jobs(worker, filepathslist)
