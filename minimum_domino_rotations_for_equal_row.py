# Charlie Miller
# Leetcode - 1007. Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

"""
First check to see if it's possible. It's only posssible
with whatever the 1st domino is. Remove possibles if it
doesn't appear in the current domino.
If both are possible, it's equivalent to only flip for one
Then check both rows - count how many match the possible value
Take the min of matches, and it's compliment to the number of dominos
(whichever we need to flip less times)
"""

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        possibles= {A[0],B[0]}
        
        for a,b in zip(A[1:],B[1:]):
            #if our possible is not in the current domino
            #it's no longer possible
            for possible in list(possibles):
                if possible not in [a,b]:
                    possibles.remove(possible)
                    
            #optimization: if there's no possibles, we can stop here
            if not possibles:
                return -1
            
        #logically equivallent if both are possible    
        value = list(possibles)[0]
        
        #check both sides of the dominoes row:
        #how many flips is required to get all equal
        min_flips = len(A)
        for dset in [A,B]:
            #how many match the possible
            matches = len([a for a in dset if a==value])
            #get the min of matches or compliment
            flips = min(matches,len(dset)-matches)
            min_flips = min(min_flips,flips)
        
        return min_flips
        