# Charlie Miller
# Leetcode - 310. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

"""
min height has to be half of the longest route from
1 side of the tree to the other. To find longest route,
first find the furthest out node from any node with bfs
Then find the route to the furthest node from the previously
found furthest node. With the route obtained, it's a matter
of finding the middle of the route. (2 middle if route has
even number of nodes)
"""

class Solution:
    #build adjacency list
    def get_adj(self,edges):
        adj = defaultdict(list)
        
        for edge in edges:
            u,v = edge[0],edge[1]
            adj[u].append(v)
            adj[v].append(u)
            
        return adj
    
    #find node furthest from source using bfs
    def find_furthest(self,n,src,adj):
        #parent is used to find the route to the furthest
        parent = [None for _ in range(n)]
        parent[src] = src
        
        #set up que
        que = [src]
        #we know furthest will be the last updated parent in bfs
        furthest = src
        while que:
            cur_node = que.pop(0)

            for neighbor in adj[cur_node]:
                #no inf backtracking
                if parent[neighbor] is not None:
                    continue
                    
                parent[neighbor] = cur_node
                que.append(neighbor)
                #furthest will be last updated neighbor
                furthest = neighbor
        
        #build route, with the furthest first
        route = [furthest]
        cur_node = furthest
        while cur_node != src:
            cur_node = parent[cur_node]
            route.append(cur_node)
        
        return route
                
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #edgecase: only 1 node
        if not edges:
            return [0]
        
        adj = self.get_adj(edges)
        
        #first find the furthest out node from any random node
        furthest = self.find_furthest(n,0,adj)[0]
        #get the route from the furthest to the other furthest
        route = self.find_furthest(n,furthest,adj)
        
        #return middle node(s)
        if len(route) % 2 != 0:
            start = len(route)//2
            end = start + 1
        else:
            start = len(route)//2 - 1
            end = start + 2
        
        return route[start:end]