# Charlie Miller
# Leetcode - 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Written 2020-04-21

"""
Find the max depth of each child. return the max of the children plus 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        #find the heights of each child        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
            
        #use the height of which ever is taller
        max_child_height = max(right_height,left_height)
        
        #+1 to count for this node itself
        return max_child_height + 1
        