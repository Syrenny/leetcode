import pytest

from src.solutions.math.reverse_integer import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("x", "expected"),
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (-1, -1),
        (1000000008, 0),
        (1000000002, 2000000001),
        (-8463847412, -2147483648),
        (-9463847412, 0),
    ],
)
def test_simple(x: int, expected: int) -> None:
    solution = Solution()
    assert solution.reverse(x) == expected
