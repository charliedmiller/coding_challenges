# Charlie Miller
# Leetcode - 1437. Check If All 1s Are at Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Written 2021-01-25

"""
Maintain a counter that keeps track of how many
more steps are needed before a 1 can be legally placed
Iterate using this counter. If a 1 is encountered while
the counter is still above zero, then the array violates
the problem condition
"""

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        #init to zero since we can legally place a 1 at the beginning
        space_ctr = 0
        
        for num in nums:
            if num == 0:
                #successfully moved a space
                space_ctr -= 1
            elif num == 1:
                
                if space_ctr > 0:
                    #condition violated
                    return False
                else:
                    #valid 1. Reset counter
                    space_ctr = k
                    
        return True
                