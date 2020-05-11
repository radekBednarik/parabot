from pathlib import PurePath, Path
from typing import Any, List, Callable, Union

import pytest

from parabot import parabot


@pytest.fixture(
    scope="session",
    params=[
        PurePath("examples/test_project_01/suite_01/suite.robot"),
        PurePath("examples/test_project_02/suite_01/suite.robot"),
    ],
)
def provide_robot_filepath(request) -> Any:
    return request.param


@pytest.fixture(scope="session", params=["reg", "smoke"])
def provide_tag(request) -> str:
    return request.param


class TestParabot(object):
    def test_path_worker(self, provide_robot_filepath) -> None:
        parabot.path_worker(provide_robot_filepath)

    def test_tag_worker(self, provide_tag) -> None:
        parabot.tag_worker(provide_tag)
