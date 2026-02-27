from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/same-tree/description
    """

    def dfs(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return f"({root.val},{left},{right})"

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ps = self.dfs(p)
        qs = self.dfs(q)

        return ps == qs
