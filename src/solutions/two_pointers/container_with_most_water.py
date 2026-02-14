from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/container-with-most-water/description
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            volume = min(height[left], height[right]) * (right - left)

            result = max(result, volume)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return result
