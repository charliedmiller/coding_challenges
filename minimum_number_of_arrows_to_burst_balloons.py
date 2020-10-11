# Charlie Miller
# Leetcode - 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

"""
Came up with sln, but was incorrect. Got a hint from
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/887586/Java-Detailed-Steps-of-Algorithm-and-Code
Approach: Sort the array by starting point.
Iterate over points - Greedily try to pull in 
as many ballons to pop and keep track of the nearest 
end point. When we pass the nearest end point of ballons
We have to start a new arrow, so add 1 to arrow count
do this to end of array and we'll have the correct number
in arrows
"""

from functools import cmp_to_key
class Solution:
    #break up ties by pulling in 2nd number in point
    def cmp(self,a,b):
        diff = a[0] - b[0]
        if diff != 0:
            return diff
        #points with lower 2nd numbers should appear first
        return a[1] - b[1]
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #edgecase: no points, so no arrows needed
        if not points:
            return 0
        
        points.sort(key=cmp_to_key(self.cmp))

        #initialize nearest end and reqd arrows
        arrows = 1
        nearest_end = points[0][1]
        
        
        for point in points:
            #unpack start and end of current point
            start = point[0]
            end = point[1]
            
            #we should start a new arrow if we pass the
            #nearest endpoint, which could be closer than previous endpoints
            nearest_end = min(nearest_end,end)
            
            #if we passed an endpoint, start a new arrow
            if start > nearest_end:
                nearest_end = end
                arrows += 1
                
        return arrows