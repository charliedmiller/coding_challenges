# Charlie Miller
# Leetcode - 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/

"""
Post order delete nodes, traversing whole tree
be sure to check if children exist since they too
could've been deleted before checking self
Pass in parent so child pointers can be cleared
(Strapped for time for more comments)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete_nodes(self,root,prev,left_right,to_delete):
        if not root:
            return
        
        self.delete_nodes(root.left,root,"left",to_delete)
        self.delete_nodes(root.right,root,"right",to_delete)
        
        if root.val in to_delete:
            if root.left:
                self.roots.append(root.left)
                
            if root.right:
                self.roots.append(root.right)
                
            if prev:
                if left_right == "left":
                    prev.left = None
                    
                if left_right == "right":
                    prev.right = None

        #Case - top root will not have a parent, and if not removed, should be added  
        elif not prev:
            self.roots.append(root)
                    
            
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.roots = []
        
        self.delete_nodes(root,None,None,to_delete)
        
        return self.roots