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

class TreeExeception(Exception):
    def __init__(self,msg,node=None):
        super().__init__(msg)
        self.node = node

class AVLTree:
    def __init__(self,printer):
        self.root = None
        self.printer = printer

    def __str__(self):
        #this class won't be implementing its own __str__ method. can be applied
        #to many kinds of trees
        return self.printer.get_str(self)


    def rotate(self,root,direction,parent):
        if direction not in ["left","right"]:
            raise TypeError("Needs to be left or right")

        di = 0 if direction == "left" else 1

        if not root:
            raise RuntimeError("No root to rotate")

        if not [root.right,root.left][di]:
            raise TreeExeception("No child for rotation",root)

        new_root = [root.right,root.left][di]
        detached_child = [new_root.left,new_root.right][di]
        if direction == "left":
            new_root.left = root
            root.right = detached_child
        else:
            new_root.right = root
            root.left = detached_child

        if root == self.root:
            self.root = new_root

        if parent is not None:
            if parent.val < new_root.val:
                parent.right = new_root
            else:
                parent.left = new_root

        return new_root 

    def balance(self,root):
        if not root:
            return root

        bias = self.get_bias(root)
        if abs(bias) <= 1:
            return root

        if bias > 0:
            child_bias = self.get_bias(root.left)
            if child_bias < 0:
                root.left = self.rotate(root.left,"left",None)
            root = self.rotate(root,"right",None)
        elif bias < 0:
            child_bias = self.get_bias(root.right)
            if child_bias > 0:
                root.right = self.rotate(root.right,"right",None)
            root = self.rotate(root,"left",None)

        return root

    def delete(self,value):
        self.root = self._delete(self.root,value)


    def _delete(self,root,value):
        if root is None:
            return None

        if value > root.val:
            root.right = self._delete(root.right,value)
        elif value < root.val:
            root.left = self._delete(root.left,value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                root = root.left
            elif root.right is not None and root.left is None:
                root = root.right
            else:
                #replace with successor, then delete successor
                cur_node = root.right
                while cur_node.left is not None:
                    cur_node = cur_node.left

                root.val = cur_node.val
                root.right = self._delete(root.right,cur_node.val)

        root = self.balance(root)
        return root

    def get_bias(self,root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        bias = left - right
        return bias
            
    def insert(self,value):
        self.root = self._insert(self.root,value)

    def _insert(self,root,value):
        if root is None:
            return Node(value)

        if root.val < value:
            root.right = self._insert(root.right,value)
        elif root.val > value:
            root.left = self._insert(root.left,value)
        else:
            return Node(value)

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



                


