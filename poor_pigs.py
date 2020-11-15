# Charlie Miller
# Leetcode - 458. Poor Pigs
# https://leetcode.com/problems/poor-pigs/
# Written 2020-11-15

"""
Solution provided by leetcode
"""

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        #how many times can we feed the pigs? More times smaller teams
        tastings = minutesToTest//minutesToDie
        
        #which pigs dies can encode what bucket it is
        teamsize = math.log(buckets,tastings+1)
        teamsize = math.ceil(teamsize)
        
        return teamsize
