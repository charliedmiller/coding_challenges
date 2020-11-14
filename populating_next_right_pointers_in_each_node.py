# Charlie Miller
# Leetcode - 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Written 2020-04-25

"""
Establish the next pointer for each node in the tree, then 
traverse each level using that pointer.
To establish next pointer, maintain a stack of the nodes that will
be assigned as the next. when traversing down, pop the stack for the
the current node's next, when traversing up (after children), push the
stack with the current node
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def recursive_connect(self,root,cur_stack):
        #at a leaf, stack should be empty
        if root is None:
            return []
        
        #current root's next is the top of the stack.
        #when there's no stack, it's null
        my_next = None
        if len(cur_stack) != 0:
            my_next = cur_stack.pop()
        root.next = my_next
        
        #assign the next for the children, going RIGHT first since
        #we're getting the nodes to the RIGHT for the stack
        cur_stack = self.recursive_connect(root.right,cur_stack)
        cur_stack = self.recursive_connect(root.left,cur_stack)
        
        #add our node to the stack for the future next
        cur_stack.append(root)
        return cur_stack
        
        
    def left_right_traversal(self,root):
        sequence = []
        
        #row node will only go right (we're in a perfect tree so this will work)
        cur_row_node = root
        #next node will traverse with the next pointer
        cur_next_node = root
        while(cur_row_node is not None):
            while(cur_next_node is not None):
                #go right on the row
                sequence.append(cur_next_node.val)
                cur_next_node = cur_next_node.next
            #we hit a null, add the #
            sequence.append("#")
            #travel down now
            cur_row_node = cur_row_node.left
            
        return sequence
    
    def connect(self, root: 'Node') -> 'Node':
        #establish the next pointers
        _ = self.recursive_connect(root,[])
        #get the sequence using the right pointers
        sequence = self.left_right_traversal(root)
        return root
        