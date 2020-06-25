"""
7. Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if (x > 2**31 - 1) or (x < -2**31):
            return 0
        else:
            if x > 0:
                reversed = ((int) (((str)(x))[::-1]))
            else:
                reversed = -1 * ((int) (((str)(-1 * x))[::-1]))
            if (reversed > 2**31 - 1) or (reversed < -2**31):
                return 0
            return reversed