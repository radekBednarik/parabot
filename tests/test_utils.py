"""
https://gist.github.com/oisinmulvihill/45c14271fad7794a4a52516ecb784e69
"""
from contextlib import contextmanager
from pathlib import Path, PurePath
from typing import Any

import pytest  # type: ignore

from parabot import parabot


@contextmanager
def not_raises(ExpectedException):
    try:
        yield

    except ExpectedException as error:
        raise AssertionError(f"Raised exception {error} when it should not!")

    except Exception as error:
        raise AssertionError(f"An unexpected exception {error} raised.")


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


@pytest.fixture(
    scope="session", params=[5, True], ids=["invalidPath1", "invalidPath2"],
)
def provide_wrong_type_robot_path(request) -> Any:
    return request.param


@pytest.fixture(scope="session")
def run_valid_get_parent_dir(provide_valid_robot_path) -> Any:
    return parabot.get_parent_dir(provide_valid_robot_path)


@pytest.fixture(scope="session")
def run_wrong_type_get_parent_dir(provide_wrong_type_robot_path) -> Any:
    return parabot.get_parent_dir(provide_wrong_type_robot_path)


class TestUtils:
    def test_valid_get_parent_dir(
        self, run_valid_get_parent_dir, provide_valid_robot_path
    ):
        path: Any = run_valid_get_parent_dir
        assert path == PurePath(provide_valid_robot_path).parent

    def test_wrong_type_get_parent_dir(self, run_wrong_type_get_parent_dir):
        with not_raises(TypeError):
            run_wrong_type_get_parent_dir
