from typing import List


class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/container-with-most-water/description
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]
            width = right - left
            best = max(best, min(h_left, h_right) * width)

            if h_left <= h_right:
                left += 1
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                right -= 1
                while left < right and height[right] <= h_right:
                    right -= 1

        return best
