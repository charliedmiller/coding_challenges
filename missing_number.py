# Charlie Miller
# Leetcode - 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Written 2020-04-21

"""
Calculate the expected sum if all numbers were there
use triangular series. Then calculate the true sum of all
numbers. The difference of these is the missing number
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_in_formula = len(nums)
        correct_sum = (num_in_formula * (num_in_formula + 1))/2
        correct_sum = int(correct_sum)
        actual_sum = sum(nums)
        diff = correct_sum - actual_sum
        if diff == 0:
            return 0
        else:
            return diff
        
        
        