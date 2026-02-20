from typing import List

import pytest

from src.solutions.math.plus_one import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("digits", "expected"),
    [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0]), ([0], [1])],
)
def test_simple(digits: List[int], expected: List[int]) -> None:
    solution = Solution()
    assert solution.plusOne(digits) == expected
