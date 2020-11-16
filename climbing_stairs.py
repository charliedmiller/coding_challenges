# Charlie Miller
# Leetcode - 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Written 2020-04-21

"""
Dynamic program - We add the number of ways 
from 1 step ago + 2 steps ago. Keep calculating these
until we reach the desired n
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        #create array of previous steps (could just use 2 vars instead of array)
        stair_combos = [0] * max((n+1),3)
        
        #base conditions
        stair_combos[1] = 1
        stair_combos[2] = 2
        if n <= 2:
            return stair_combos[n]
        
        #calculate all steps up to n
        for step in range(3,n+1):
            stair_combos[step] = stair_combos[step-1] + stair_combos[step-2]
            
        return stair_combos[n]
        