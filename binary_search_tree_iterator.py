# Charlie Miller
# Leetcode - 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/
# Written 2020-12-09

"""
Maintain a stack for nodes we still need to traverse
When next is called, pop the stack and get the node's value,
but also add to the stack the node's right ancestor, and all
left successors of that node - to preserve inorder traversal
The stack will only be empty once all nodes have been traversed
so we can use this to indicate hasNext
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        #add to stack the root and all left ancestors
        self.stack = []        
        cur_node = root
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left

    def next(self) -> int:
        #get next node (at top of stack) and value
        node = self.stack.pop()
        result = node.val
        
        #add the node's right child, and all its left ancestors
        cur_node = node.right
        while cur_node:
            self.stack.append(cur_node)
            cur_node = cur_node.left
            
        return result

    def hasNext(self) -> bool:
        #if the stack has nodes, there will be a next
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()