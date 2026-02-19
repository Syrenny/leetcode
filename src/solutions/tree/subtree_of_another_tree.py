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
        https://leetcode.com/problems/subtree-of-another-tree/description
    """

    def treeToStr(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "#"

        return f"({root.val},{self.treeToStr(root.left)},{self.treeToStr(root.right)})"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        main_tree = self.treeToStr(root)
        sub_tree = self.treeToStr(subRoot)

        return sub_tree in main_tree
