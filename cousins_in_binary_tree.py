# Charlie Miller
# Leetcode - 993. Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/

"""
Find the depth and parent for the desired nodes
Find out if they fullfil the conditions for cousins
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #return a tuple of depth, and the parent. Add up depth 
    # on the way out
    def find_node(self,root,parent,target):
        if root is None:
            return None
        
        #base case: found target, depth is 0 but will be added up
        if root.val == target:
            return (0,parent)
        
        #if target was found in left, add up depth and return new depth
        left = self.find_node(root.left,root,target)
        if left is not None:
            depth = left[0] + 1
            node = (depth,left[1])
            return node
        
        #same as left but for right
        right = self.find_node(root.right,root,target)
        if right is not None:
            depth = right[0] + 1
            node = (depth,right[1])
            return node
        
        #target was not found here
        return None
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #find nodes, showing depth,parent
        x_node = self.find_node(root,None,x)
        y_node = self.find_node(root,None,y)
        
        #not same depth
        if x_node[0] != y_node[0]:
            return False
        
        #same parent
        if x_node[1] == y_node[1]:
            return False
        
        return True