from collections import deque
from typing import Iterable, Optional

import pytest

from src.solutions.tree.same_tree import Solution, TreeNode


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


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


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("p", "q", "expected"),
    [
        (build_tree([1, 2, 3]), build_tree([1, 2, 3]), True),
        (build_tree([1, 2]), build_tree([1, None, 2]), False),
        (build_tree([1, 2, 1]), build_tree([1, 1, 2]), False),
        (build_tree([None]), build_tree([None]), True),
        (build_tree([1]), build_tree([None]), False),
    ],
)
def test_simple(p: Optional[TreeNode], q: Optional[TreeNode], expected: bool) -> None:
    solution = Solution()
    assert solution.isSameTree(p, q) == expected
