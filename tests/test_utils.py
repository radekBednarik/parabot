from pathlib import Path, PurePath
from typing import Any, List

import pytest

from parabot import utils


@pytest.fixture(
    scope="session",
    params=[
        Path("examples/test_project_01/suite_01/suite.robot"),
        Path("examples/test_project_02/suite_01/suite.robot"),
    ],
)
def provide_path(request) -> Any:
    return request.param


@pytest.fixture(
    scope="session",
    params=[
        PurePath("examples/test_project_01/suite_01/suite.robot"),
        PurePath("examples/test_project_02/suite_01/suite.robot"),
    ],
)
def provide_pure_path(request) -> Any:
    return request.param


@pytest.fixture(
    scope="session",
    params=["examples/test_project_01/suite_01", "examples/test_project_02/suite_01"],
)
def provide_rel_dirpath(request) -> str:
    return request.param


class TestUtils(object):
    def test_get_parent_dir(self, provide_path) -> Any:
        parent: Any = utils.get_parent_dir(provide_path)
        assert parent == PurePath(provide_path).parent

    def test_get_all_robot_files(self) -> List[Any]:
        files: List[Any] = utils.get_all_robot_files()
        assert len(files) > 0
        assert isinstance(files[0], Path)

    def test_create_output_folder(self, provide_pure_path) -> Any:
        output_fold_path: Any = utils.create_output_folder(
            provide_pure_path, "suite.robot"
        )
        assert isinstance(output_fold_path, PurePath)
        assert len(str(output_fold_path)) > 0

    def test_get_spec_robot_files(self, provide_rel_dirpath) -> List[Any]:
        list_of_paths: List[Any] = utils.get_specific_robot_files_by_paths(
            provide_rel_dirpath
        )
        assert len(list_of_paths) > 0
        assert isinstance(list_of_paths[0], Path)
