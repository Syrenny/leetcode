from __future__ import annotations

from bisect import bisect_left
from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/last-stone-weight/description
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)

        while len(stones) > 1:
            x, y = stones.pop(), stones.pop()

            if x == y:
                continue

            new = abs(x - y)

            i = bisect_left(stones, new)

            stones.insert(i, new)

        if stones:
            return stones[0]

        return 0
