from typing import List

import pytest

from src.solutions.dynamic.min_cost_climbing_stairs import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("cost", "expected"),
    [([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6), ([10, 15], 10)],
)
def test_simple(cost: List[int], expected: int) -> None:
    solution = Solution()
    assert solution.minCostClimbingStairs(cost) == expected
