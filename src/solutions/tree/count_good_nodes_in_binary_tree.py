from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/count-good-nodes-in-binary-tree/description
    """

    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]

        good = 0

        while stack:
            node, greatest = stack.pop()

            if node.val >= greatest:
                good += 1
                greatest = node.val

            if node.left is not None:
                stack.append((node.left, greatest))

            if node.right is not None:
                stack.append((node.right, greatest))

        return good
