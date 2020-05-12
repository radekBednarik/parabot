from pathlib import PurePath, Path
from typing import Any, List, Callable, Union, Optional

import pytest  # type: ignore

from parabot import parabot  # type: ignore


@pytest.fixture(
    scope="session",
    params=[
        PurePath("examples/test_project_01/suite_01/suite.robot"),
        PurePath("examples/test_project_02/suite_01/suite.robot"),
    ],
    ids=["path1", "path2"],
)
def provide_robot_filepath(request) -> Any:
    return request.param


@pytest.fixture(scope="session", params=["reg", "smoke"])
def provide_tag(request) -> str:
    return request.param


@pytest.fixture(scope="module")
def run_path_worker(provide_robot_filepath) -> Optional[int]:
    result: Optional[int] = parabot.path_worker(provide_robot_filepath)
    return result


@pytest.fixture(scope="module")
def run_tag_worker(provide_tag) -> Optional[int]:
    result: Optional[int] = parabot.tag_worker(provide_tag)
    return result


class TestParabot(object):
    def test_path_worker(self, run_path_worker):
        status: Optional[int] = run_path_worker
        assert status == None

    def test_tag_worker(self, run_tag_worker):
        status: Optional[int] = run_tag_worker
        assert status == None

    # def test_path_worker(self, provide_robot_filepath):
    #     status: Optional[int] = parabot.path_worker(provide_robot_filepath)
    #     assert status is None

    # def test_tag_worker(self, provide_tag):
    #     status: Optional[int] = parabot.tag_worker(provide_tag)
    #     assert status is None
