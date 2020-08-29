# Charlie Miller
# Leetcode - 1561. Maximum Number of Coins You Can Get
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

"""
Always give Bob the smallest of the remaining piles - he'll take the
lower 3rd of the pile. There's no way to trick Alice into giving us
the largest of the remaining, but we can always take the second largest
That's why we skip 1 for the iteration
"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        #sort first 
        piles.sort()
        
        #bob gets the last third
        bob_set = len(piles)//3
        
        #Alice will get the largest, so we stride with 2 over the remainings
        return sum(piles[bob_set::2])
        