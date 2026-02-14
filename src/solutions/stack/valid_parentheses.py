from collections import deque


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/valid-parentheses/description
    """

    def isValid(self, s: str) -> bool:
        stack: deque[str] = deque([])

        brackets = {"(": ")", "{": "}", "[": "]"}

        for ch in s:
            if ch in brackets.keys():
                stack.appendleft(ch)
                continue

            if len(stack) == 0:
                return False

            opening = stack.popleft()

            if brackets[opening] != ch:
                return False

        if len(stack) != 0:
            return False

        return True
