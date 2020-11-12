# Charlie Miller
# Leetcode - 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Written 2020-04-25

"""
Serialize: serialize children, then add root value before children
null child is represented by None. This creates a preorder traversal sequence

Deserialize - dequeue the sequence, create a node with it,
pass the sequence to left then right, then attach children. Return the full node
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def traverse_serialize(self,root):
        #use non to indicate leaf for parent
        if root is None:
            return [None]
        
        #generate sequences for children
        left_seq = self.traverse_serialize(root.left)
        right_seq = self.traverse_serialize(root.right)
        
        #add current nodes value before the children's sequence
        seq = [root.val] + left_seq + right_seq
        return seq
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #obtain the preorder sequence
        sequence = self.traverse_serialize(root)
        #stringify, then cut off [ and ]
        string = str(sequence)    
        return string[1:-1]

    def int_or_None(self,val):
        val = val.strip()
        if val == "None":
            return None
        else:
            return int(val)
    
    def traverse_deserialize(self,seq):
        cur_val = seq.pop(0)
        #parent had a leaf on this side. No further work
        if cur_val is None:
            return None
        
        cur_node = TreeNode(cur_val)
        #create children nodes with the same seq. then attach to current
        cur_node.left = self.traverse_deserialize(seq)
        cur_node.right = self.traverse_deserialize(seq)
        return cur_node
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #obtain a list of values from the comma separated list
        sequence = list(map(self.int_or_None,data.split(",")))
        #generate based off sequence
        root = self.traverse_deserialize(sequence)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))