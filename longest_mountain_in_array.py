# Charlie Miller
# Leetcode - 845. Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/
# Written 2020-11-16

"""
Maintain a finite state machine to keep track of
mountain heights, while iterating through the array
3 states: 
await_trough: not counting array bc prev number couldn't be
part of a valid mountain
increasing: counting array, but won't consider for max mountain height
bc there has to be a decrease
decreasing: can only ocurr after increasing, count in the array. Ends in
decreasing will be considered for max mountain height
Maintain a count of the mountain size, and the max seen mountain size
"""

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        max_seen = 0
        #edgecase: arr less than 3 - impossible for a mountain to form
        if len(A) < 3:
            return max_seen
        
        #initialize state and state register
        prev = A[0]
        state = "await_trough"
        cur_mtn = 0
        valid_mtn = False
        
        for num in A[1:]:
            if state == "await_trough":
                #can only start counting if we see an increase
                if num > prev:
                    state = "increasing"
                    #this and prev are part of the mountain
                    cur_mtn = 2
                    
            elif state == "increasing":
                if num > prev:
                    cur_mtn += 1
                elif num < prev:
                    #prev was the peak now we decrease, and now a valid mountain
                    cur_mtn += 1
                    state = "decreasing"
                    valid_mtn = True
                else:
                    #plateaus illegitimize mountains, so we have to start
                    #from scratch
                    cur_mtn = 0
                    valid_mtn = False
                    state = "await_trough"
                    
            elif state == "decreasing":
                if num < prev:
                    cur_mtn += 1
                elif num > prev:
                    #a trough detected. We must record the length of the
                    #mountain, but now count the prev towards the next mtn
                    max_seen = max(max_seen,cur_mtn)
                    valid_mtn = False
                    cur_mtn = 2
                    state = "increasing"
                else:
                    #plateaus mark ends of mountains. Since it's not
                    #an increase, we have to go back to await_trough
                    max_seen = max(max_seen,cur_mtn)
                    valid_mtn = False
                    cur_mtn = 0
                    state = "await_trough"
                    
            else:
                print("Invalid State reached!!")
                return 0
            
            prev = num
        
        #consider the last recorded mountain (since we didn't have a chance before)
        #but only consider it if it was valid (last decreasing)
        if valid_mtn:
            max_seen = max(max_seen,cur_mtn)
                    
                
        return max_seen
        