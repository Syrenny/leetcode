import pytest

from src.solutions.stack.valid_parentheses import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("s", "expected"),
    [("()", True), ("()[]{}", True), ("(]", False), ("([])", True), ("([)]", False), ("(", False), ("a", False)],
)
def test_simple(s: str, expected: int) -> None:
    solution = Solution()
    assert solution.isValid(s) == expected
