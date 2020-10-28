# Charlie Miller
# Leetcode - 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

"""
Iterate over the array
Keep track of the start and end of contiguous ranges
We know if a range is contiguous if the current is 1 more
than the previous number. In cases where range is 1 number,
we add to input as specified by the problem
"""

class Solution:
    def add_to_output(self,start,end,output):
        #add range to output according to problem spec
        if end == start:
            range_str = "%d" % end
        else:
            range_str = "%d->%d" % (start,end)

        output.append(range_str)
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        
        #cannot operate correctly if no numbers return here
        if not nums:
            return output
        
        #keep track of the start of a range, as well as prev num seen
        start = nums[0]
        prev = nums[0]
        
        for num in nums[1:]:
            #There's a break in continuum, so we'll add this range
            if (num-1) != prev:
                #range will be the start and the previous number
                self.add_to_output(start,prev,output)           
                #current number is the start of a new range
                start = num
                
            prev = num
        
        #the array terminated, so our last range must also terminate
        self.add_to_output(start,prev,output)
        
        return output
        
