"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        else:
            curLength = len(s)
            maxLength = len(s)
            
            while curLength > 1:
                startIndex = 0
                endIndex = startIndex + curLength
                while endIndex <= maxLength:
                    substring = s[startIndex:endIndex]
                    if substring == substring[::-1]:
                        return substring
                    startIndex += 1
                    endIndex += 1
                curLength -= 1

            return s[0]