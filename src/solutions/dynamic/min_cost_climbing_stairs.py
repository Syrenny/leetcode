from __future__ import annotations

from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/min-cost-climbing-stairs/description
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0, 0, 0]

        for step in range(2, length + 1):
            cur = step % 3
            prev1 = (step - 1) % 3
            prev2 = (step - 2) % 3

            dp[cur] = min(
                dp[prev1] + cost[step - 1],
                dp[prev2] + cost[step - 2],
            )

        return dp[length % 3]
