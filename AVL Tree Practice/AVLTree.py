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
        return self.printer.get_str(self)


    def rotate(self,root,direction,parent):
        if direction not in ["left","right"]:
            raise TypeError("Needs to be left or right")

        di = 0 if direction == "left" else 1

        if not root:
            raise RuntimeError("No root to rotate")

        if not [root.right,root.left][di]:
            raise TreeExeception("No right child for left rotation",root)

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
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                #replace with successor, then delete successor
                cur_node = root.right
                while cur_node.left is not None:
                    cur_node = cur_node.left

                root.val = cur_node.val
                root.right = self._delete(root.right,cur_node.val)
                return root

        root = self.balance(root)
        return root

    def get_bias(self,root):
        if not root:
            return 0
            
        left = self.height(root.left)
        right = self.height(root.right)

        bias = left - right
        return bias

    def balance(self,root):
        bias = self.get_bias(root)
        if abs(bias) <= 1:
            return

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

    def insert(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        if self.find(self.root,value) is not None:
            return

        cur_node = self.root
        parent1,parent2,parent3,parent4 = None,None,None,None

        while cur_node:
            parent4 = parent3
            parent3 = parent2
            parent2 = parent1
            parent1 = cur_node

            if cur_node.val < value:
                cur_node = cur_node.right
            elif cur_node.val > value:
                cur_node = cur_node.left
            else:
                raise RuntimeError("Value found in tree despite find claiming it not there")

        if parent1.val < value:
            parent1.right = new_node
        else:
            parent1.left = new_node


        if parent2 and self.current_balance(parent2) > 1:
            self.rebalance(parent2,parent3,value)
        elif parent3 and self.current_balance(parent3) > 1:
            self.rebalance(parent3,parent4,value)



    def rebalance(self,root,parent,value):
        path = ""
        cur_node = root

        while cur_node.val != value:
            if cur_node.val < value:
                path += "r"
                cur_node = cur_node.right

            elif cur_node.val > value:
                path += "l"
                cur_node = cur_node.left
            
            else:
                raise RuntimeError("Improper implementation")

        path = path[:2]

        first_child = root.right if root.val < value else root.left

        if path == "l":
            self.rotate(root,"right",parent)
        elif path == "r":
            self.rotate(root,"left",parent)
        elif path == "ll":
            self.rotate(root,"right",parent)
        elif path == "rr":
            self.rotate(root,"left",parent)
        elif path == "rl":
            self.rotate(first_child,"right",root)
            self.rotate(root,"left",parent)
        elif path == "lr":
            self.rotate(first_child,"left",root)
            self.rotate(root,"right",parent)
        else:
            raise RuntimeError("Improper Implementation")

        
    def current_balance(self,node):
        left = self.height(node.left)
        right = self.height(node.right)

        return abs(left-right)


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



                


