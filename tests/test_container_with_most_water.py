from typing import List

import pytest

from src.solutions.two_pointers.container_with_most_water import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("height", "expected"),
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1), ([0, 1], 0)],
)
def test_simple(height: List[int], expected: int) -> None:
    solution = Solution()
    assert solution.maxArea(height) == expected
