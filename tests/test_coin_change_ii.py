from typing import List

import pytest

from src.solutions.dynamic.coin_change_ii import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("amount", "coins", "expected"),
    [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1), (0, [], 1), (5000, [5000, 1], 2)],
)
def test_simple(amount: int, coins: List[int], expected: int) -> None:
    solution = Solution()
    assert solution.change(amount, coins) == expected
