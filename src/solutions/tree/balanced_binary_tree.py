from __future__ import annotations

from typing import Optional

from common.tree import TreeNode


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/balanced-binary-tree/description
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = dfs(node.left)

            if left == -1:
                return -1

            right = dfs(node.right)

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left + 1, right + 1)

        return dfs(root) != -1
