from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/diameter-of-binary-tree/description
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def rec(node: Optional[TreeNode]) -> int:
            nonlocal answer

            if node is None:
                return 0

            left_height = rec(node.left)
            right_height = rec(node.right)

            answer = max(answer, left_height + right_height)

            return max(left_height, right_height) + 1

        rec(root)

        return answer
