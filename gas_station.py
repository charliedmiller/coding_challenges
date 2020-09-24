# Charlie Miller
# Leetcode - 134. Gas Station
# https://leetcode.com/problems/gas-station/

"""
This is a max circular subarray problem in disguise (i.e. can be reduced to)
First, we can describe a gas station by the net gallons of gas it can provide 
(gas - distance to next). A solution will only exist if the sum of all nets is
0 or greater - otherwise there's a deficit somewhere. When there's a sln, it will
be at the start of the max circular subarray of the nets - gain most gas before largest
deficits. 

This will either be 1) the max subarray non-circular or 2)the inverse of the
min subarray non-circular, whichever is greater. To find the max subarray non-circular,
iterate thru each element, the max subarray will either include the current, or will start
anew with the current. Keep track of the max seen subarray
"""

class Solution:
    #find the largest subarray, non-circular
    def largest_subarray(self,arr):
        #keep track of beginning, end, and the value
        max_seen = arr[0]
        max_start = 0
        max_end = 1
        
        #for current iteration
        cur_sum = arr[0]
        start = 0
        
        for i,num in enumerate(arr[1:]):
            #since we started at 1, i is +1
            i += 1
            
            
            cur_sum += num
            
            #start a new subarray when the prev sum is too low
            if num > cur_sum:
                cur_sum = num
                start = i
            
            #keep track largest seen subarray
            if cur_sum > max_seen:
                max_start = start
                max_end = i+1   #end is non-inclusive
                max_seen = cur_sum
                
        return max_seen,max_start,max_end
        
    def largest_circular_subarray_start(self,arr):
        #finding min subarray is same as max inversed subarr
        neg_arr = [0-e for e in arr]
        
        in_val,in_start,_ = self.largest_subarray(arr)
        neg_val,_,neg_end = self.largest_subarray(neg_arr)
        
        #when max subarray is not wrapped, it's the normal largest subarray non-circular
        #when it is wrapped, the min subarray non-circular will be farther from zero 
        #than the normal max subarr
        if in_val < neg_val:
            #the start will be the end of min subarray
            start = neg_end % len(arr)
        else:
            start = in_start
            
        return start
        
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #get all the net values
        nets = [g-c for g,c in zip(gas,cost)]

        #if the whole circuit nets less than 0, it's impossible
        if sum(nets) < 0:
            return -1
        
        #the solution will always start at the beginning of the max circular subarray
        start = self.largest_circular_subarray_start(nets)
        
        return start
        