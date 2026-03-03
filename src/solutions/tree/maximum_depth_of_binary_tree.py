from __future__ import annotations

from typing import Optional

from common.tree import TreeNode


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/maximum-depth-of-binary-tree/description
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)
