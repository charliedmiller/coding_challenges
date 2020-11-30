# Charlie Miller
# AVL Tree Implementation (practice)
# Written 2020-11-22


class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return str(self.val)

#include the node in a tree exception
class TreeExeception(Exception):
    def __init__(self,msg,node=None):
        super().__init__(msg)
        self.node = node

class AVLTree:
    def __init__(self,printer):
        self.root = None
        self.printer = printer #we will delegate our __str__ to this class

    def __str__(self):
        #this class won't be implementing its own __str__ method. can be applied
        #to many kinds of trees
        return self.printer.get_str(self)


    def rotate(self,root,direction):
        #direction affects which nodes to access in routine
        if direction not in ["left","right"]:
            raise TypeError("Needs to be left or right")

        di = 0 if direction == "left" else 1

        if not root:
            raise RuntimeError("No root to rotate")

        #when rotating, we are choosing one of the children to be in its place
        #direction depending. Raise error if that child isn't found 
        if not [root.right,root.left][di]:
            raise TreeExeception("No child for rotation",root)

        #new root will be chosen. One child of that new root will become a child of
        #the old root
        new_root = [root.right,root.left][di]
        detached_child = [new_root.left,new_root.right][di]

        #swap places with new root and detached
        if direction == "left":
            new_root.left = root
            root.right = detached_child
        else:
            new_root.right = root
            root.left = detached_child

        #be sure to update AVL root if we're at the top
        if root == self.root:
            self.root = new_root

        return new_root 

    def balance(self,root):
        """ 
        Rotate nodes to help balance the tree. The node may change after this
        returns the node in the place of the node in the arg
        """
        #a non existant node is balanced
        if not root:
            return root

        #if bias is within normal limits, don't do anything
        bias = self.get_bias(root)
        if abs(bias) <= 1:
            return root


        if bias > 0:
            #if the heavy side has a bias in the opposite direction, we need
            #to rotate an additional time to align with the overal bias
            child_bias = self.get_bias(root.left)
            if child_bias < 0:
                root.left = self.rotate(root.left,"left")
            #rotate in the opposite direction of the bias
            root = self.rotate(root,"right")
        elif bias < 0:
            child_bias = self.get_bias(root.right)
            if child_bias > 0:
                root.right = self.rotate(root.right,"right")
            root = self.rotate(root,"left")

        #after rotations, root might have changed. Report that change
        return root

    #adapt to internal method
    def delete(self,value):
        self.root = self._delete(self.root,value)


    def _delete(self,root,value):
        if root is None:
            return None

        #assign root children as new value, since children may change 
        #after deletion
        if value > root.val:
            root.right = self._delete(root.right,value)
        elif value < root.val:
            root.left = self._delete(root.left,value)
        else:
            # we need to delete this node
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                root = root.left
            elif root.right is not None and root.left is None:
                root = root.right
            else:
                #this node has 2 children (above have less)
                #replace with successor, then delete successor
                cur_node = root.right
                while cur_node.left is not None:
                    cur_node = cur_node.left

                root.val = cur_node.val
                root.right = self._delete(root.right,cur_node.val)

        #rebalance, if necessary
        root = self.balance(root)
        return root

    def get_bias(self,root):
        """
        Find the difference in height of children of root. 
        Positive bias means left heavy, opposite for right
        """
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        bias = left - right
        return bias
            
    #adapt for internal method
    def insert(self,value):
        self.root = self._insert(self.root,value)

    
    def _insert(self,root,value):
        #we found location where value should be
        if root is None:
            return Node(value)

        #children may change after insertion. Calls will report this change
        #traverse down the bst
        if root.val < value:
            root.right = self._insert(root.right,value)
        elif root.val > value:
            root.left = self._insert(root.left,value)
        else:
            return root

        #rebalance if necessary
        root = self.balance(root)

        return root


    def find(self,root,value):
        if not root:
            return None

        if root.val < value:
            return self.find(root.right,value)
        elif root.val > value:
            return self.find(root.left,value)
        else:
            return root


    def height(self, root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)
        return max(left,right) + 1



                


