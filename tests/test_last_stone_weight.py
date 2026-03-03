from typing import List

import pytest

from src.solutions.array.last_stone_weight import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("stones", "expected"),
    [([2, 7, 4, 1, 8, 1], 1), ([1], 1)],
)
def test_simple(stones: List[int], expected: int) -> None:
    solution = Solution()
    assert solution.lastStoneWeight(stones) == expected
