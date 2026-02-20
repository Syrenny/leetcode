from __future__ import annotations


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/climbing-stairs/description/
    """

    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            for step in [1, 2]:
                if i - step < 0:
                    continue

                dp[i] += dp[i - step]

        return dp[n]
