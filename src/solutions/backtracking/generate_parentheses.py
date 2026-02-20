from __future__ import annotations

from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/generate-parentheses/description
    """

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(open_used: int, close_used: int, path: list[str]):
            if open_used == n and close_used == n:
                answer.append("".join(path))
                return

            if open_used < n:
                backtrack(open_used + 1, close_used, path + ["("])

            if close_used < open_used:
                backtrack(open_used, close_used + 1, path + [")"])

        backtrack(0, 0, [])

        return answer
