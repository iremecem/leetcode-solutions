"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            longest = 0
            for i in range (len(s)):
                for j in range (len(s), i - 1, -1):
                    substring = s[i:j]
                    noRepeat = True
                    for k in substring:
                        if (substring.count(k) > 1):
                            noRepeat = False
                            break
                    if noRepeat and len(substring) > longest:
                        longest = len(substring)
            return longest