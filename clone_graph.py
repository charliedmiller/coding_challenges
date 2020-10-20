# Charlie Miller
# Leetcode - 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

"""
Do a bfs of the original graph. Create new nodes
when encountered by the neighbor list.
Add neighbors only when we are examining that current node
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #Edge case: no nodes
        if not node:
            return None
        
        #queue for bfs
        queue = [node]
        #we will return this as the top of the graph
        top = Node(node.val)
        #use this hash as a visited tool but also to
        #get nodes that were previously created
        new_nodes = {node.val:top}
        
        while queue:
            #old node
            cur_node = queue.pop(0)
            #new node
            cur_new_node = new_nodes[cur_node.val]
            for neighbor in cur_node.neighbors:
                if neighbor.val not in new_nodes:
                    #node never seen, create it and add to queue
                    new_node = Node(neighbor.val)
                    new_nodes[neighbor.val] = new_node
                    add_neighbor = new_node
                    queue.append(neighbor)
                else:
                    #we've seen it so only add it to the neighbors list
                    add_neighbor = new_nodes[neighbor.val]
                    
                cur_new_node.neighbors.append(add_neighbor)
                
        return top