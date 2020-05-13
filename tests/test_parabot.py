from pathlib import PurePath, Path
from typing import Any, List, Callable, Union, Optional

import pytest  # type: ignore

from parabot import parabot  # type: ignore


@pytest.fixture(
    scope="session",
    params=[
        PurePath("examples/test_project_01/suite_01/suite.robot"),
        PurePath("examples/test_project_02/suite_01"),
    ],
    ids=["valid_path1", "valid_path2"],
)
def provide_valid_robot_filepath(request) -> Any:
    return request.param


@pytest.fixture(
    scope="session",
    params=[
        PurePath("examples/test_pro_01/suite_01/suite.robot"),
        PurePath("examples/test_project_02/suite_0"),
    ],
    ids=["invalid_path1", "invalid_path2"],
)
def provide_invalid_robot_filepath(request) -> Any:
    return request.param


@pytest.fixture(scope="session", params=["reg", "smoke", ""])
def provide_valid_tag(request) -> str:
    return request.param


@pytest.fixture(scope="session", params=["regg", "smokes"])
def provide_invalid_tag(request) -> str:
    return request.param


@pytest.fixture(scope="session")
def run_valid_path_worker(provide_valid_robot_filepath) -> Optional[int]:
    result: Optional[int] = parabot.path_worker(provide_valid_robot_filepath)
    return result


@pytest.fixture(scope="session")
def run_invalid_path_worker(provide_invalid_robot_filepath) -> Optional[int]:
    result: Optional[int] = parabot.path_worker(provide_invalid_robot_filepath)
    return result


@pytest.fixture(scope="session")
def run_valid_tag_worker(provide_valid_tag) -> Optional[int]:
    result: Optional[int] = parabot.tag_worker(provide_valid_tag)
    return result


@pytest.fixture(scope="session")
def run_invalid_tag_worker(provide_invalid_tag) -> Optional[int]:
    result: Optional[int] = parabot.tag_worker(provide_invalid_tag)
    return result


class TestParabot(object):
    def test_path_worker_valid(self, run_valid_path_worker):
        status: Optional[int] = run_valid_path_worker
        assert status == None

    def test_path_worker_invalid(self, run_invalid_path_worker):
        status: Optional[int] = run_invalid_path_worker
        assert status == 1

    def test_tag_worker_valid(self, run_valid_tag_worker):
        status: Optional[int] = run_valid_tag_worker
        assert status == None

    def test_tag_worker_invalid(self, run_invalid_tag_worker):
        status: Optional[int] = run_invalid_tag_worker
        assert status == 1
