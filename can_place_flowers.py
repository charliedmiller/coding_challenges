# Charlie Miller
# Leetcode - 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/
# Written 2020-12-05

"""
Greedily place flowers whenever you can. Not placing
when you can flowers will always result in punishment
Iterate over the flowerbed, keep track of the remaining
flowers. Decrement remaining and mark the flowerbed when
we find a spot where a flower can be placed
"""

class Solution:
    def get_prev(self,flowerbed,i):
        """
        Return 0 if out of range. else flowerbed[i]
        """
        if i == 0:
            return 0
        
        return flowerbed[i-1]
    
    def get_next(self,flowerbed,i):
        """
        Return 0 if out of range. else flowerbed[i]
        """
        if i == len(flowerbed) - 1:
            return 0
        
        return flowerbed[i+1]
        
    def canPlaceFlowers(self,flowerbed,n):
        #Edgecase: no flowers to place. So we're good
        if n == 0:
            return True
        
        remaining = n
        for i,cur_bed in enumerate(flowerbed):
            #we cannot place if theres a flower here or in an
            #adjacent flower
            if (cur_bed == 1 or self.get_next(flowerbed,i) == 1 
                             or self.get_prev(flowerbed,i) == 1):
                continue
                
            #this is a spot we can place. So place it
            flowerbed[i] = 1
            remaining -= 1
            
            #Return true early if we've fulfilled our requirement
            if remaining == 0:
                return True
            
        #all places have been exhausted and there are still remaining flowers. 
        #cannot be done
        return False