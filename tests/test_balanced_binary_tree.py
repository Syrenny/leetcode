from typing import Optional

import pytest

from common.tree import TreeNode, build_tree
from src.solutions.tree.balanced_binary_tree import Solution


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("root", "expected"),
    [
        (build_tree([3, 9, 20, None, None, 15, 7]), True),
        (build_tree([1, 2, 2, 3, 3, None, None, 4, 4]), False),
        (build_tree([]), True),
    ],
)
def test_simple(root: Optional[TreeNode], expected: bool) -> None:
    solution = Solution()
    assert solution.isBalanced(root) == expected
