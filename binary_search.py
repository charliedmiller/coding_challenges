# Charlie Miller
# Leetcode - 704. Binary Search
# https://leetcode.com/problems/binary-search/

"""
check the midpoint. 
If it's higher, discard the right half
if it's lower, discard the left half
otherwise it's the target, return the idx

When the bounds meet, then we know the target
doesn't exist
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #bounds for left and right half
        start = 0
        end = len(nums)
        
        while start != end:
            #derive midpoint from the bounds
            mid = start + (end - start)//2
            
            
            if nums[mid] > target:
                #discard right half
                end = mid
            elif nums[mid] < target:
                #discard left half
                start = mid+1
            else:
                #we found our target
                return mid
            
        #bounds have met, so target does not exist
        return -1