# Charlie Miller
# Leetcode - 897. Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/submissions/
# Written 2020-12-03

"""
Do an inorder traversal, keeping track of 2 things:
The root of the inorder tree
The last node of the inorder tree
For each node visited, add it as the right child of
the last node in the inorder tree. Then return the
head of the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def create_increasingBST(self,root):
        if not root:
            return
        
        #inorder. Do left first
        self.create_increasingBST(root.left)
        
        #clear out this node's left as defined by problem
        root.left = None
        
        #this is the first node. Simply assign the head and last
        if self.inorder_last is None:
            self.inorder_head = root
            self.inorder_last = root
        #this is not first. Add root as the right child of the last    
        else:
            self.inorder_last.right = root
            #catch up to the new last
            self.inorder_last = self.inorder_last.right
            
        #Inorder. do right child now
        self.create_increasingBST(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        #keep track of the head and last nodes of the inorder tree
        self.inorder_head = None
        self.inorder_last = None
        #do the inorder traversal
        self.create_increasingBST(root)
        return self.inorder_head