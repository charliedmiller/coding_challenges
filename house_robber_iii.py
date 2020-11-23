# Charlie Miller
# Leetcode - 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Written 2020-11-23

"""
For each node, decide whether or not to rob.
In cases where the previous house was robbed,
force the decision to not rob this time. Return
the max of both choices. Each subtree is a subproblem,
so we can take advantage of a dp memo. Add the results
of the children to the current node for each choice
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob_tree(self,root,robbed_prev):
        #can't rob a house that's not there
        if not root:
            return 0
        
        #retreive result if already calculated
        hashable = str(id(root)) + str(robbed_prev)
        if hashable in self.dp:
            return self.dp[hashable]
        
        #Find out max possible result for each child if we DON'T rob
        dont_rob = self.rob_tree(root.left,False) + self.rob_tree(root.right,False)
        
        #find out max possible result if we do.
        #if we robbed previous, we'll get caught and all money is lost
        rob_this = 0
        if not robbed_prev:
            #pass along to children that we DID rob thier previous
            left = self.rob_tree(root.left,True)
            right = self.rob_tree(root.right,True)
            #add their max possible, plus our spoils from this node
            rob_this = left + right + root.val
            
        #figure out which is the better choice
        max_goods = max(dont_rob,rob_this)
        
        #record and return our results
        self.dp[hashable] = max_goods
        return max_goods
        
    def rob(self, root: TreeNode) -> int:
        self.dp = {}
        return self.rob_tree(root,False)