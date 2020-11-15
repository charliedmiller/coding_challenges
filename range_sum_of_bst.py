# Charlie Miller
# Leetcode - 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# Written 2020-11-15

"""
Normal tree sum except filter out those
that don't fall into the range. Normal
tree sum requires to add the current node's value
to the sums of the left and right subtrees. Leaves
are just the value of its node itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #not a valid node - the sum is automatically 0
        if not root:
            return 0
        
        
        #find the sums of the subtrees
        left = self.rangeSumBST(root.left,low,high)
        right = self.rangeSumBST(root.right,low,high)
        
        #conditions on whether to add the current node's value
        root_in_range =  low <= root.val and root.val <= high
        
        #add node's value only if it satisfies the conditions
        root_contribution = root.val if root_in_range else 0
        
        #return sum of left, right, and current node values
        return left + right + root_contribution