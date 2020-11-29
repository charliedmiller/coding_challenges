# Charlie Miller
# Leetcode - 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/
# Written 2020-11-29

"""
Each index is like a node in a graph, and the value shows the edges.
With this model, the problem reduces to: Can we reach a node with
value 0 with the current start node? This can be solved with a simple bfs
Time: O(n), Space: O(n) - queue
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #edgecase: there are no 0s
        if 0 not in arr:
            return False
        
        #initialize queue and visited array
        queue = [start]
        arr_size =len(arr)
        visited = [False for _ in range(arr_size)]
        visited[start] = True
        
        #edgecase: We already started at 0!
        if arr[start] == 0:
            return True
        
        while queue:
            cur_i = queue.pop(0)
            #get neighbors
            left = cur_i - arr[cur_i]
            right = cur_i + arr[cur_i]
            
            for neighbor in [left,right]:
                #cannot jump outside arr
                if neighbor < 0 or neighbor > (arr_size-1):
                    continue
                
                #shouldn't revisit neighbors, else inf loop
                if visited[neighbor]:
                    continue
                
                #we found a 0!
                if arr[neighbor] == 0:
                    return True
                
                #mark neighbor as visited and add to queue
                visited[neighbor] = True
                queue.append(neighbor)
                
        #we've exhausted all nodes reachable from start. No 0's found
        return False