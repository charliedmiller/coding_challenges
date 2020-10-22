# Charlie Miller
# Leetcode - 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

"""
recursivley find the min depth of left and right children.
Keep track of min depth seen so we don't have to venture 
futher than necessary
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_depth(self,root,cur_depth,max_depth):
        #case: one child is null, so we return inf
        if not root:
            return float("inf")
        
        #optimization:stop if we've gone deeper than some other child
        if cur_depth > max_depth:
            return max_depth
        
        #we found a leaf. Return its depth 
        #(we already know its shorter than what we've seen before)
        if not root.left and not root.right:
            return cur_depth
        
        
        left_depth = self.min_depth(root.left,cur_depth+1,max_depth)
        #left child can be shorter than what we've seen before. update it like so
        max_depth = min(left_depth,max_depth)
        right_depth = self.min_depth(root.right,cur_depth+1,max_depth)
        
        #right child could be shorter, give the shorter of max_depth, left child, and right child
        return min(right_depth,max_depth)
        
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.min_depth(root,1,float("inf"))