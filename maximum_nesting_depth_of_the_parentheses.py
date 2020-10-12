# Charlie Miller
# Leetcode - 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

"""
Keep a stack counter. 
When ( encountered add 1
When ) encountered subtract 1
keep track of the highest stack counter is seen
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        max_seen = 0
        for char in s:
            #increase counter    
            if char == "(":
                stack += 1
            #decrease counter
            elif char == ")":
                stack -= 1
                
            max_seen = max(max_seen,stack)
            
        return max_seen