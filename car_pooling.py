# Charlie Miller
# Leetcode - 1094. Car Pooling
# https://leetcode.com/problems/car-pooling/

"""
Sort the trips in order of who gets picked up first
Maintain a priority queue for the ends of each trip, annotate 
by how much capacity will increase at the end. Iterate over
the trips, add capacity when ends are reached, remove capacity
when we pick up. If at any point capacity goes below 0, then
it won't be possible
Time O(n)
Space O(n)
"""

import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sort by start location
        trips.sort(key=lambda x:x[1])
        
        #priority queue
        ends = []
        for trip in trips:
            #Before we pick up, drop off any who's end location is before the current
            #start location. <= since we can drop off before picking up at the same loc
            while ends and ends[0][0] <= trip[1]:
                ending_trip = heapq.heappop(ends)
                capacity += ending_trip[1]
                
            #pick up, and add the end location to the priority queue
            heapq.heappush(ends,(trip[2],trip[0]))
            
            #capacity decreases when customers are picked up
            capacity -= trip[0]
            
            
            if capacity < 0:
                return False
            
        #No more pick ups, so we know we can do the trips
        return True