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
            longest = 1
            curLength = len(s)
            maxLength = len(s)
            
            while curLength > 1:
                startIndex = 0
                endIndex = startIndex + curLength
                while endIndex <= maxLength:
                    substring = s[startIndex:endIndex]
                    noRepeat = True
                    for k in substring:
                        if (substring.count(k) > 1):
                            noRepeat = False
                            break
                    if noRepeat:
                        return curLength
                    startIndex += 1
                    endIndex += 1
                curLength -= 1

            return longest