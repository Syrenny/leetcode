from typing import Optional

import pytest

from common.tree import TreeNode, build_tree
from src.solutions.tree.maximum_depth_of_binary_tree import Solution


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
        (build_tree([3, 9, 20, None, None, 15, 7]), 3),
        (build_tree([1, None, 2]), 2),
        (build_tree([]), 0),
        (build_tree([None]), 0),
    ],
)
def test_simple(root: Optional[TreeNode], expected: int) -> None:
    solution = Solution()
    assert solution.maxDepth(root) == expected
