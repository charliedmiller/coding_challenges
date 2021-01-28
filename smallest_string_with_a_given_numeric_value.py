# Charlie Miller
# Leetcode - 1663. Smallest String With A Given Numeric Value
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
# Written 2021-01-28

"""
This can be modeled like filling n glasses with k units of water. 
Start by filling each glass with 1 unit, afterwards keep filling the
right most glasses until they reach capacity of 26. Determine how
many will be filled entirely, how much the last filled will be at
when all water has been exahausted, and the rest. this will determine
zs, the transition letter, and as respectively
"""

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        #edgecase: all glasses are filled. There is no transition or a's
        if k == (26 * n):
            return "z" * n
        
        #first fill each glass with 1 unit
        remaining = k - n
        
        #determine how many will be filled entirely
        required_zs = remaining//25
        
        #how much will the first glass not filled entirely will have?
        transition = remaining % 25 + 1
        #convert to character
        transition_char = chr(transition + 96)
            
        #determine number of a's (-1 to account for transition glass)
        required_as = (n - required_zs) - 1
        
        #build
        string = ("a" * required_as) + transition_char + ("z" * required_zs)
        return string