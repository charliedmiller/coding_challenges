# Charlie Miller
# Leetcode - 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# Written 2020-11-27

"""
Find the sum. If it's odd return False
Sort, descending. If the highest element is
higher than half of the sum, also return False
Afterwards, find a subset in the array that adds
up to exactly half of the sum. Recursively try new
numbers to add (skipping ones that will go over the
target, and keeping a memo of previous iterations).
Return False if all combinations have been exhausted
"""

class Solution:
    def can_sum_to(self,nums,start,target):
        #return result if seen before
        hashable = (start,target)
        if hashable in self.memo:
            return self.memo[hashable]
        
        #we found a combination!
        if target == 0:
            return True
        
        #we exhausted all options before reaching the target
        if start >= len(nums):
            return False
        
        #pick the next element to choose. See if it works
        prev = None
        for i,num in enumerate(nums[start:]):
            #do not choose a number that goes over our target
            if num > target:
                continue
                
            #optimization: do not pick this number if we've already
            #tried it before (wouldn't be here if it didn't work)
            if prev is not None and num == prev:
                continue
                
            #when chosing this number, we can only choose numbers after this
            #(we know all prev options are not viable)
            new_start = start + i + 1
            # If we use this number, our target will decrease
            new_target = target-num 
            if self.can_sum_to(nums,new_start,new_target):
                self.memo[hashable] = True
                return True

            prev = num
            
        #record for future calls
        self.memo[hashable] = False
        return False
    
    def canPartition(self, nums: List[int]) -> bool:
        #Cannot partition if sum is odd
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        nums.sort(reverse=True)
        #our target is half of the sum
        target = total//2
        #if any element is larger than half, we can't partition
        if nums[0] > target:
            return False
        
        self.memo = {}
        #see if we can use a subset to add up to half - implies other will also be half
        return self.can_sum_to(nums,1,target-nums[0])