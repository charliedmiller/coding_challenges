# Charlie Miller
# Leetcode - 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
#Written 5/9/2020

"""
create a hash with the jewels, iterate over stones
to count how many jewels there are
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #can be acheived with a hashset too
        jewels = {j:1 for j in J}
        
        #iterate over stones
        num_jewels = 0
        for stone in S:
            num_jewels += jewels.get(stone,0)
            
        return num_jewels
        
        