from typing import Any
from pathlib import PurePath, Path

import pytest  # type: ignore

from parabot import parabot


@pytest.fixture(
    scope="session",
    params=[
        Path("examples/test_project_01/suite_01/suite.robot"),
        Path("examples/test_project_02/suite_01/suite.robot"),
    ],
    ids=["validPath1", "validPath2"],
)
def provide_valid_robot_path(request) -> Any:
    return request.param


@pytest.fixture(scope="session")
def run_valid_get_parent_dir(provide_valid_robot_path) -> Any:
    return parabot.get_parent_dir(provide_valid_robot_path)


class TestUtils:
    def test_valid_get_parent_dir(
        self, run_valid_get_parent_dir, provide_valid_robot_path
    ):
        path: Any = run_valid_get_parent_dir
        assert path == PurePath(provide_valid_robot_path).parent
