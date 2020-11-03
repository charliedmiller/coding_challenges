# Charlie Miller
# 1446. Consecutive Characters
# https://leetcode.com/problems/consecutive-characters/

"""
Keep track of current power by seeing if the character
is the same as the last. Return the max power encountered
"""

class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        
        #init
        max_power = 1
        prev = s[0]
        cur_power = 1
        
        for char in s[1:]:
            #same as last time, just increase power
            if char == prev:
                cur_power += 1
            else:
                #new char encountered, match the power with max seen
                max_power = max(max_power,cur_power)
                #reset power for next set
                cur_power = 1
                
            prev = char
        
        #matchup power of last set of chars
        max_power = max(max_power,cur_power)
        
        return max_power
        