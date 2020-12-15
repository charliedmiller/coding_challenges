# Charlie Miller
# Leetcode - 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Written 2020-12-13

"""
Annotate each node with the max height of that subtree
Then progress down the children with the higher height.
If both children have the same height, then we've reached
the common ancestor of the deepest nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self,root):
        """return the height. But if it's a null, return 0"""
        if not root:
            return 0
        
        return self.heights[root.val]
    
    def populate_heights(self,root):
        """Annotate the height of each node"""
        if not root:
            return 0
        
        left = self.populate_heights(root.left)
        right = self.populate_heights(root.right)
        
        height = max(left,right) + 1
        
        #We can use a hash since all nodes will have unique values
        self.heights[root.val] = height
        return height
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.heights = {}
        #annotate all the heights of each node
        self.populate_heights(root)
        
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        cur_node = root

        #keep traversing down the tree until the left and right 
        #child heights are the same
        while left_height != right_height:
            #traverse down in the direction of the taller tree
            if left_height > right_height:
                cur_node = cur_node.left
            elif right_height > left_height:
                cur_node = cur_node.right
                
            #get the heights of the new children
            left_height = self.get_height(cur_node.left)
            right_height = self.get_height(cur_node.right)
            
            
        return cur_node