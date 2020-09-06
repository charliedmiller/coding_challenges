#Charlie Miller
#Leetcode - All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Create 2 iterators for inorder traversal
Grab the smallest value from either iterator, and advance if taken
continue until both iterators are exhusted
Space complexity O(h) where h is height of tallest tree
time complexity O(n) where n is total number of elements
"""


class Solution:
    #iterator for inorder traversal
    def iterate_tree(self,root):
        if not root:
            #if no tree return an empty iterator
            return
        
        #Do a iterative dfs, yes this modifies the tree afterwards
        cur_node = root
        stack = [root]
        
        while stack:
            cur_node = stack[-1]
            
            #Search left first
            if cur_node.left:
                stack.append(cur_node.left)
                #modify so we know not to go here after we're done here
                cur_node.left = None
                continue
                
            #Do our inorder here
            yield cur_node.val
            stack.pop()
            
            #serach right afterwards
            if cur_node.right:
                stack.append(cur_node.right)
            
    #wrap next exception in a function, return sentinel when done
    def get_next(self,iterator):
        try:
            return next(iterator)
        except StopIteration:
            return float("inf")
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        merged = []
        
        #get iterators
        tree1_iter = self.iterate_tree(root1)
        tree2_iter = self.iterate_tree(root2)
        
        #booleans to tell when we're done
        tree1_done = False
        tree2_done = False
        
        #get inaugural values
        t1_next = self.get_next(tree1_iter)
        t2_next = self.get_next(tree2_iter)
        
        while not (tree1_done and tree2_done):
        
            #iterate tree where most recent value was taken
            if t1_next < t2_next:
                merged.append(t1_next)
                t1_next = self.get_next(tree1_iter)
            else:
                merged.append(t2_next)
                t2_next = self.get_next(tree2_iter)
    
            #check if we're done
            tree1_done = t1_next == float("inf")
            tree2_done = t2_next == float("inf")


            
        return merged
                