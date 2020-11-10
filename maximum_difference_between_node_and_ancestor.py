# Charlie Miller
# Leetcode - 1026. Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Written 9/11/2020

"""
Recursively traverse tree. Keep track of min and max numbers seen
find the diff between the current nodes value and the min/max numbers
find also the max difference for each child, making the current value
the min/max seen if appropriate
Return the max difference for all of these
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_ancestor_diff(self,root,max_seen,min_seen,max_diff):
        if not root:
            #just return the max difference seen so far
            return max_diff
        
        #see if the current nodes value creates a bigger diff
        #than seen so far
        max_diff = max(abs(max_seen - root.val),abs(min_seen - root.val),max_diff)
        #update max/min for child calls
        max_seen = max(max_seen,root.val)
        min_seen = min(min_seen,root.val)
        left = self.max_ancestor_diff(root.left,max_seen,min_seen,max_diff)
        right = self.max_ancestor_diff(root.right,max_seen,min_seen,max_diff)
        
        #return the max of what we saw, and what children saw
        return max(left,right,max_diff)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        #edgecase: no root - so diff is 0
        if not root:
            return 0
        
        return self.max_ancestor_diff(root,root.val,root.val,0)