from pathlib import PurePath, Path
from typing import Any, List, Union, Optional

import pytest  # type: ignore

from parabot import parabot


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


@pytest.fixture(scope="session", params=["reg", "smoke"])
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


@pytest.fixture(scope="session")
def run_valid_pool_path_workers() -> Union[List[Optional[int]], int]:
    return parabot.pool_path_workers(
        parabot.path_worker,
        [
            Path("examples/test_project_01/suite_01/suite.robot"),
            Path("examples/test_project_02/suite_01/suite.robot"),
        ],
        timeout=60,
    )


@pytest.fixture(scope="session")
def run_timeout_pool_path_workers() -> Union[List[Optional[int]], int]:
    return parabot.pool_path_workers(
        parabot.path_worker,
        [
            Path("examples/test_project_01/suite_01/suite.robot"),
            Path("examples/test_project_02/suite_01/suite.robot"),
        ],
        timeout=5,
    )


@pytest.fixture(scope="session")
def run_valid_pool_tag_workers() -> List[Optional[int]]:
    return parabot.pool_tag_workers(parabot.tag_worker, ["reg", "smoke"])


class TestParabotWorkers:
    def test_path_worker_valid(self, run_valid_path_worker):
        status: Optional[int] = run_valid_path_worker
        assert status is None

    def test_path_worker_invalid(self, run_invalid_path_worker):
        status: Optional[int] = run_invalid_path_worker
        assert status == 1

    def test_tag_worker_valid(self, run_valid_tag_worker):
        status: Optional[int] = run_valid_tag_worker
        assert status is None

    def test_tag_worker_invalid(self, run_invalid_tag_worker):
        status: Optional[int] = run_invalid_tag_worker
        assert status == 1


class TestParabotPools:
    def test_valid_pool_path_workers(self, run_valid_pool_path_workers):
        status: List[Optional[int]] = run_valid_pool_path_workers
        assert 1 not in status

    def test_timeout_pool_path_workers(self, run_timeout_pool_path_workers):
        status: int = run_timeout_pool_path_workers
        assert status == 1

    def test_valid_pool_tag_workers(self, run_valid_pool_tag_workers):
        status: List[Optional[int]] = run_valid_pool_tag_workers
        check: List[bool] = []

        for stat in status:
            if stat == 0:
                check.append(True)
            else:
                check.append(False)

        assert all(check) is True
