# Charlie Miller
# Leetcode - 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Written 2020-12-11

"""
Rewrite array without the triplicates. Keep track of a writing index.
While iterating over the array, write to this index with the current value
Advance the index if no triplicates found. DO NOT advance if triplicate found
that way it will be overwritten by either a valid value, or futher duplicates
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        #init prev and repeats to detect triplicates
        prev = nums[0]
        repeats = 0
        
        #first value will always be valid
        write_idx = 1
        remove_duplicate = False #triplicate detected
        
        for num in nums[1:]:
            nums[write_idx] = num
            
            #duplicate detected
            if num == prev:
                #we only need to remove triplicates
                repeats += 1
                if repeats > 1:
                    #triplicate detected
                    remove_duplicate = True
            else:
                #reset repeat counter if new number found
                repeats = 0

            #Do not advance duplicate if triplicate found
            #that way it will be overwritten by valid values
            if not remove_duplicate:
                write_idx += 1
                
            #reset triplicate detection
            remove_duplicate = False
            prev = num

        #all valid values have been written. Anything after that is not valid
        nums = nums[:write_idx]
        
        return len(nums)
                