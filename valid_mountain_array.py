# Charlie Miller
# Leetcode - 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/
# Written 2020-12-10

"""
Iterate over the array and keep track of the
previous element to tell if we're increasing or
decreasing in value. We can never plataeu.
We can never increase after starting to decrease
We must acheive both increasing and decreasing for 1
full iteration to be considered a mountain
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #according to rules, any arr of length lower than 3 is not
        if len(arr) < 3:
            return False
        
        #initialize state
        prev = arr[0]
        state = "increasing"
        
        #both of these must be true in order to be considered a mountain
        increased = False
        decreased = False
        
        for num in arr[1:]:
            if state == "increasing":
                #noticed a decrease in values
                if num < prev:
                    state = "decreasing"
                    decreased = True
                elif num == prev:
                    #cannot plateau
                    return False
                else:
                    #this will be false if arr is always decreasing
                    increased = True
                    
            elif state == "decreasing":
                #cannot plataeu or increase again
                if num >= prev:
                    return False
            else:
                print("invalid state")
                
            prev = num
            
        #we must have both increased and decreased
        return increased and decreased
            