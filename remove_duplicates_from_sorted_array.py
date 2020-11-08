# Charlie Miller
# Leetcode - 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Written 4/20/2020

"""
Array is sorted so we only have to check the previous element
to determine if it's a duplicate
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = None
        i = 0
        while(i < len(nums)):
            if nums[i] == prev_num:
                #deleting already advances the array, so
                #we don't increment i to "double" advance
                del nums[i]
            else:
                prev_num = nums[i]
                i += 1
                
        return len(nums)
        