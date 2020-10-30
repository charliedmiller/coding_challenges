# Charlie Miller
# Leetcode - 849. Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/
    
"""
3 choices: Sit at the rightmost chair, leftmost chair,
or somewhere in the middle. We'll always sit in the middle
of a gap, but count ourself as part of the distance. Get the 
distance from the left first, max of middle gaps, and right last
return the max of all 3
"""    

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_dist = None
        right_dist = None
        middle_dist = 0
        
        #use this to count distance to next person
        empty_count = 0
        
        for seat in seats:
            #only increase count if empty
            if seat == 0:
                empty_count +=1
                continue
                
            #we found a non-empty. If the first time, assign left distance
            if left_dist is None:
                left_dist = empty_count
            else:
                #otherwise it's a middle gap. count ourselves for distance (ceil)
                dist = math.ceil(empty_count/2)
                middle_dist = max(middle_dist,dist)
                
            #reset empty counter
            empty_count = 0
            
        #right dist is the remaining empty seats to the right
        right_dist = empty_count
        
        return max(left_dist,right_dist,middle_dist)