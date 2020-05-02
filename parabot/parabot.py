from io import StringIO
from multiprocessing import Process, get_context
from typing import Any, Callable, List

from robot.run import run

from parabot.utils import (
    create_output_folder,
    get_all_robot_files,
    get_parent_dir,
    get_specific_robot_files_by_paths,
    parse_args,
)


def path_worker(filepath: Any) -> None:
    """Worker used by Pool.

    Runs instance of RobotFramework for given .robot file.
    
    Arguments:
        filepath {Any} -- python PurePath to .robot file to be executed by robot.run.run
    
    See:
        https://docs.python.org/3/library/pathlib.html
        https://robot-framework.readthedocs.io/en/v3.1.2/autodoc/robot.html#module-robot.run
    """
    basepath: Any = get_parent_dir(filepath)
    stdout: Any = StringIO()
    run(
        filepath, outputdir=create_output_folder(basepath, filepath.name), stdout=stdout
    )
    print(stdout.getvalue())
    stdout.close()


def tag_worker(tag: str) -> None:
    """Worker used by Process.

    Runs instance of RobotFramework for given tag.
    
    Arguments:
        tag {str} -- tag
    
    See:
        https://robot-framework.readthedocs.io/en/v3.1.2/autodoc/robot.html#module-robot.run
    """
    stdout: Any = StringIO()
    run(
        "./",
        outputdir=create_output_folder("./reports/", tag),
        include=[tag],
        stdout=stdout,
    )
    print(stdout.getvalue())
    stdout.close()


def pool_path_workers(path_worker: Callable, filepathslist: List[Any]) -> None:
    """Runs path_worker against list of arguments in parallel.

    Max. number of parallel processes is limited by no. of CPUs cores.
    
    Arguments:
        path_worker {Callable} -- path_worker function
        filepathslist {List[Any]} -- list of python PurePaths to .robot files
    """
    with get_context("spawn").Pool(maxtasksperchild=1) as p:
        p.map_async(path_worker, filepathslist).get(60)


def pool_tag_workers(tag_worker: Callable, tags: List[str]) -> None:
    """Runs tag_worker against list of tags in parallel.

    For each tag is spawned one process.
    
    Arguments:
        tag_worker {Callable} -- tag_worker function
        tags {List[str]} -- list of tags 
    """
    procesess: List[Any] = []

    for tag in tags:
        p: Any = Process(target=tag_worker, args=(tag,))
        p.start()
        procesess.append(p)
    # I am NOT really shure about this, but it works.
    # Will welcome any clarification or corrections.
    [proc.join() for proc in procesess]


def main() -> None:
    """Main function.

    See:
        https://stackoverflow.com/questions/30487767/check-if-argparse-optional-argument-is-set-or-not
    """
    filepathslist: List[Any]
    args: Any = parse_args()

    if args.all:
        filepathslist = get_all_robot_files()
        pool_path_workers(path_worker, filepathslist)

    if args.folders is not None:
        filepathslist = get_specific_robot_files_by_paths(args.folders)
        pool_path_workers(path_worker, filepathslist)

    if args.tags is not None:
        pool_tag_workers(tag_worker, args.tags)


if __name__ == "__main__":
    main()
