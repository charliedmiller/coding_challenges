# Charlie Miller
# Leetcode - 169. Majority Element
# https://leetcode.com/problems/majority-element/

"""
Solved on 4/25/2020
Calculate what constitutes as majority - 1 more than half
Keep track of th frequencies for each number.
When any frequencies pass the majority threshhold, return that number
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #calculate majority threshold (1 more than floor of half)
        majority_threshold = int(len(nums)/2) + 1
        
        #determine frequencies
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
            
            #we reached the threshold so we can stop here
            if freqs[num] == majority_threshold:
                return num
        