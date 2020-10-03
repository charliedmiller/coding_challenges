# Charlie Miller
# Leetcode - 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

"""
keep two indicies: left and right
advance right when the difference is smaller than or equal to k
advance left when difference is larger than k
only advance right when right next to each other
only advance left if right can't advance no more
get the diff of values at left and right and keep track of the k-diffs
do this on a unique set
in the case of 0 diff, find out how many numbers have duplicates
Time: O(n), Space: O(n) since creating sets
"""


class Solution:
    def num_duplicates(self,nums):
        
        pairs = 0
        seen = set()
        paired = set()
        
        for num in nums:
            #only add pairs if we've seen it before
            if num not in seen:
                seen.add(num)
            else:
                #to prevent counting triplicates or more, add to another set
                #to check before adding to pairs
                if num not in paired:
                    pairs += 1
                    paired.add(num)
                    
        return pairs
                
    def findPairs(self, nums: List[int], k: int) -> int:
        #edge case: k is 0, must do different routine
        if k == 0:
            return self.num_duplicates(nums)
        
        
        #remove duplicates
        nums = list(set(nums))
        
        #edge case: there's only 1 or less numbers, so it must be 0
        if len(nums) < 2:
            return 0
        
        #numbers must be sorted in order for left right advance to work        
        nums.sort()
        
        pairs = 0
        
        #init indexes
        left = 0
        right = 1
        
        while left < (len(nums) - 1):
            #check if it's a k-diff pair
            cur_diff = nums[right] - nums[left]
            if cur_diff == k:
                pairs += 1
                
            #check for edge cases first, then normal cases
            
            #can't advance right
            if right == len(nums) -1:
                #optimization: we know the rest will be smaller than k, so we can stop here
                if cur_diff <= k:
                    return pairs
                else:
                    left += 1
            
            # left cannot be same as right, so advance right
            elif left+1 == right:
                right += 1
            
            #advance right if smaller or equal (to give space to make smaller)
            elif cur_diff <= k:
                right += 1
            else:
                left += 1
                
        return pairs
                
        