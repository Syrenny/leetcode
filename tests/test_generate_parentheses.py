from typing import List

import pytest

from src.solutions.backtracking.generate_parentheses import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("n", "expected"),
    [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])],
)
def test_simple(n: int, expected: List[str]) -> None:
    solution = Solution()
    assert set(solution.generateParenthesis(n)) == set(expected)
