import pytest

from src.solutions.dynamic.climbing_stairs import Solution


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
    [(2, 2), (3, 3), (1, 1)],
)
def test_simple(n: int, expected: int) -> None:
    solution = Solution()
    assert solution.climbStairs(n) == expected
