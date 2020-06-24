"""
4. Median of Two Sorted Arrays
Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0
        mergedList = []
        
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                mergedList.append(nums1[index1])
                index1 += 1
                if index1 == len(nums1):
                    break
            if nums2[index2] < nums1[index1]:
                mergedList.append(nums2[index2])
                index2 += 1
        
        while index2 < len(nums2):
            mergedList.append(nums2[index2])
            index2 += 1   
        while index1 < len(nums1):
            mergedList.append(nums1[index1])
            index1 += 1 
         
        mergedLength = len(mergedList)
        if (mergedLength % 2 == 1):
            return mergedList[((int) (mergedLength / 2))]
        return (mergedList[(int)(mergedLength / 2)] + mergedList[((int)(mergedLength / 2)) - 1] ) / 2  