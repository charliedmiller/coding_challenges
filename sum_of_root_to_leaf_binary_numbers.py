# Charlie Miller
# Leetcode - 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

import copy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Keep track of each path to the leaves. 
When a leaf is encountered, combine the path to form the binary number
add the binary number to a list of all leaf numbers encountered
once the entire tree is traversed, sum all leaf numbers
"""


class Solution:
    #keep track of paths
    def add_to_numbers(self,root,path):
        
        #parent had only 1 child, we don't do anything here
        if not root:
            return
        
        #add the current value to our path
        #must deepcopy, otherwise the whole tree will be in the path
        path = copy.deepcopy(path)
        path.append(str(root.val))
        
        #when encounter a leaf, determine the binary number from the path, and
        #add it to our total numbers
        if not root.left and not root.right:
            num = int(''.join(path),2)
            self.numbers.append(num)
            return
        
        #we're not a leaf, so we continue
        self.add_to_numbers(root.left,path)
        self.add_to_numbers(root.right,path)
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        #init array for our routine to put numbers into when
        #leaves are encountered
        self.numbers = []
        self.add_to_numbers(root,[])
        
        #return the sum
        return sum(self.numbers)