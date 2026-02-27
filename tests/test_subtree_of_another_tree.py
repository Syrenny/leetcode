from __future__ import annotations

from typing import Optional

import pytest

from common.tree import build_tree
from src.solutions.tree.subtree_of_another_tree import Solution, TreeNode


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("root", "subRoot", "expected"),
    [
        (build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2]), True),
        (
            build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
            build_tree([4, 1, 2]),
            False,
        ),
        (build_tree([1]), build_tree([1]), True),
        (build_tree([1]), build_tree([2]), False),
        (build_tree([1]), build_tree([1, 2]), False),
        (build_tree([2, 1]), build_tree([1]), True),
        (build_tree([12]), build_tree([2]), False),
    ],
)
def test_simple(
    root: Optional[TreeNode], subRoot: Optional[TreeNode], expected: int
) -> None:
    solution = Solution()
    assert solution.isSubtree(root, subRoot) == expected
