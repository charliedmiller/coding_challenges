# Charlie Miller
# Leetcode - 1217. Minimum Cost to Move Chips to The Same Position
# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

"""
Given a zero cost to move 2, we only need to count how many
have an even or odd position. Move every chip with the same
alignment together for free,then move the smaller stack to 
the larger. The cost is the size of the smaller stack, which
is the smaller of even or odd aligned
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        #count even and odd positions
        evens, odds = 0, 0
        for chip in position:
            if chip % 2 == 0:
                evens += 1
            else:
                odds += 1
                
        #return the smaller of even or odds
        return min(evens,odds)