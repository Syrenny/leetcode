from __future__ import annotations

from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/plus-one/description
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        care = 1

        i = len(digits) - 1
        while care != 0 and i >= 0:
            if digits[i] + 1 > 9:
                digits[i] = 0
                care = 1
            else:
                digits[i] += 1
                care = 0
            i -= 1

        if care == 1:
            return [1] + digits

        return digits
