# Charlie Miller
# Leetcode - 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Written 2020-12-16

"""
Traverse whole tree, maintaining what would be the min and max
values the tree nodes could be. e.g. every value in the right
subtree of a node must be more than that node's value, and
every value in the left subtree of a node must be less than that 
node's value. When traversing down, update the min and max accordingly
If any node breaks these rules, we know it's not a valid BST anymore
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def valid_BST(self,root,max_val,min_val):
        #an empty subtree is a valid BST
        if not root:
            return True
        
        #check if the node's values fall in the BST constraints
        if root.val <= min_val or root.val >= max_val:
            return False
        
        #check if left subtree is a valid BST
        left = self.valid_BST(root.left,root.val,min_val)
        
        #no need to check right if we already know it's an invalid tree
        if not left:
            return False
        
        #check that right is also valid.
        right = self.valid_BST(root.right,max_val,root.val)
        
        # This subtree is valid if the right is also valid
        return right
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid_BST(root,float("inf"),float("-inf"))