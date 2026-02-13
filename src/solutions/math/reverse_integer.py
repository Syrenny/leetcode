class Solution:
    """LeetCode problem

    Link:
        https://leetcode.com/problems/reverse-integer/description/
    """

    def reverse(self, x: int) -> int:
        minimum, maximum = "2147483648", "2147483647"
        maxlen = 10
        is_negative = True if x < 0 else False

        x = abs(x)
        digits = str(x)
        digits = digits[::-1]
        digits = digits.lstrip("0") or "0"

        length = len(digits)
        if length > maxlen:
            return 0
        elif length == maxlen:
            bound = minimum if is_negative else maximum

            if digits > bound:
                return 0

        if is_negative:
            digits = "-" + digits

        return int(digits)
