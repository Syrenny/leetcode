from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/coin-change-ii
    """

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for value in range(coin, amount + 1):
                dp[value] += dp[value - coin]

        return dp[amount]
