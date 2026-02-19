from __future__ import annotations

from collections import deque
from typing import Iterable, Optional

import pytest

from src.solutions.tree.subtree_of_another_tree import Solution, TreeNode


def build_tree(values: Iterable[Optional[int]]) -> Optional[TreeNode]:
    it = iter(values)
    try:
        root_val = next(it)
    except StopIteration:
        return None

    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue: deque[TreeNode] = deque([root])

    while queue:
        node = queue.popleft()

        try:
            left_val = next(it)
        except StopIteration:
            break
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


def tree_to_level_order(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Serialize a binary tree into level-order list (trim trailing None's)."""
    if root is None:
        return []

    out: list[Optional[int]] = []
    queue: deque[Optional[TreeNode]] = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue

        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while out and out[-1] is None:
        out.pop()

    return out


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
