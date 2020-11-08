# Charlie Miller
# Leetcode - 563. Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt/

"""
find the total sum of each sub-tree, then find the
tilt for each one, accumulate each tilt
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_tilt(self,root):
        if not root:
            return 0
        
        #get total sum for children
        left = self.find_tilt(root.left)
        right = self.find_tilt(root.right)
        
        #find current root's tilt, as defined by the problem
        cur_tilt = abs(left - right)
        self.total_tilt += cur_tilt
        
        #return the total sum for this tree to help parents find their tilt
        tree_sum = left + right + root.val
        return tree_sum
    
    def findTilt(self, root: TreeNode) -> int:
        #accumulate all tilts here
        self.total_tilt = 0
        self.find_tilt(root)
        return self.total_tilt