from __future__ import annotations

from collections import deque
from typing import Iterable, Optional


class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


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
