"""
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []
        for num in nums:
            firstIndex = nums.index(num)
            complementary = target - num
            if complementary in nums:
                if not (nums.count(num) == 1 and complementary == num):
                    secondIndex = nums.index(complementary, firstIndex + 1)
                    return [firstIndex, secondIndex]
        return []