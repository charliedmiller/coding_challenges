# Charlie Miller
# Leetcode - 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Written 2021-01-26

"""
Perform a dijkstra search while keeping track
of the largest effort step so far. Edge costs
are the efforts as defined by the problem
"""

import heapq
class Solution:
    def valid(self,x,y):
        if x < 0 or y < 0:
            return False
        
        if x > self.max_x or y > self.max_y:
            return False
        
        return True
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #edgecase: no graph
        if not heights:
            return 0
        
        self.max_y = len(heights) - 1
        self.max_x = len(heights[0]) - 1
        
        #initialize priority queue
        routes = [(0,(0,0))]
        
        #efforts is here so we don't introduce paths with more required effort into the heap
        efforts = [[float("inf") for _ in range(self.max_x +1)] for __ in range(self.max_y +1)]

        #initialize step tracker which will be our result
        max_step = 0
        
        #dijkstra
        while len(routes) > 0:
            effort, cur_coordinates = heapq.heappop(routes)
            cx,cy = cur_coordinates

            #do not process if this is an outdated node discovery
            if efforts[cy][cx] < effort:
                continue
    
            #this is a step we will might have to take, see if it's the largest so far
            max_step = max(max_step,effort)
            
            #we found our exit spot
            if cur_coordinates == (self.max_x,self.max_y):
                break
            
            #generate neighbors to consider
            neighbors = [
                (cx+1,cy),
                (cx-1,cy),
                (cx,cy+1),
                (cx,cy-1)
            ]
            
            for nx,ny in neighbors:
                #make sure the neighbor is a valid coordinate
                if not self.valid(nx,ny):
                    continue
                    
                #calculate effort required to move to this spot
                reqd_effort = abs(heights[cy][cx] - heights[ny][nx])
                
                #only proceed if this is a strictly better path than seen before
                if reqd_effort >= efforts[ny][nx]:
                    continue
                
                #add to priority queue and record effort required
                heapq.heappush(routes,(reqd_effort,(nx,ny)))
                efforts[ny][nx] = reqd_effort
                               
                               
        return max_step