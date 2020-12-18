# Charlie Miller
# Leetcode - 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
# Written 2020-12-18

"""
Keep track of the lowest seen, and what ever is
the lowest above the lowest - middle. If we ever
see a value above middle we've found a tuple.
If we find a value above lowest we update middle,
but only after checking if it's above the current mid
we update lowest last. Keep doing this until the arr
is exhuasted
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #cannot have a 3 tuple with less than 3 elements
        if len(nums) < 3:
            return False
        
        #init trackers
        lowest = nums[0]
        mid = None
        
        for num in nums[1:]:
            #check if we've found the last in the tuple
            if mid is not None and num > mid:
                return True

            #update mid or lowest
            if num > lowest:
                mid = num
            elif num < lowest:
                lowest = num
                
        #array has been exhausted. No tuple found
        return False
        