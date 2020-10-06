# Charlie Miller
# Leetcode - 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""
Recursively check if the current node is larger or smaller than the value
Stop when the current node is null (should TreeNode here). In this case
return the newly created node, otherwise return the root
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        #we've reached the bottom. Insert here
        if not root:
            return TreeNode(val)
        
        #advance to left child if less, otherwise advance right
        #ok to do just else since == is guaranteed to never happen
        #assign child, in case of a new leaf being created
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
            
                
        return root
        