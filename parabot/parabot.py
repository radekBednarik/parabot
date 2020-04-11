from multiprocessing import Pool
from typing import Any, Callable, List

from robot.run import run

from parabot.utils import (
    get_all_robot_files,
    get_specific_robot_files_by_paths,
    parse_args,
    get_parent_dir,
    create_output_folder,
)


def worker(filepath: Any) -> None:
    """Worker used by Pool.

    Runs instance of RobotFramework for given .robot file.
    
    Arguments:
        filepath {Any} -- python PurePath to .robot file to be executed by robot.run.run
    
    See:
        https://docs.python.org/3/library/pathlib.html
        https://robot-framework.readthedocs.io/en/v3.1.2/autodoc/robot.html#module-robot.run
    """
    basepath: Any = get_parent_dir(filepath)
    run(filepath, outputdir=create_output_folder(basepath, filepath.name))


def pool_jobs(worker: Callable, filepathslist: List[Any]) -> None:
    """Runs worker against list of arguments in parallel.

    Max. number of parallel processes is limited by no. of CPUs cores.
    
    Arguments:
        worker {Callable} -- worker function
        filepathslist {List[Any]} -- list of python PurePaths to .robot files
    """
    with Pool(maxtasksperchild=1) as p:
        p.map(worker, filepathslist)


def main() -> None:
    """Main function.
    """
    filepathslist: List[Any]
    args: Any = parse_args()

    if args.all:
        filepathslist = get_all_robot_files()
        pool_jobs(worker, filepathslist)

    elif hasattr(args, "folders"):
        filepathslist = get_specific_robot_files_by_paths(args.folders)
        pool_jobs(worker, filepathslist)
