# Charlie Miller
# Hackerrank - Level Order traversal
# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

"""
Create an array where each element i represents all values seen 
left to right at height i.
Do a preorder traversal to get the correct left to right order
Keep track of height during traversal to append to correct level
"""


values = []
seen_height = 0

def level_order(root,cur_height):
    global seen_height

    if not root:
        return

    #Append to the values array if we've reach deeper than ever before
    #otherwise append to the array of the corresponding level
    if cur_height > seen_height:
        values.append([root.info])
        seen_height = cur_height
    else:
        values[cur_height-1].append(root.info)

    #Append seen value first, then the same for children, keeping track of height
    level_order(root.left,cur_height+1)
    level_order(root.right,cur_height+1)

def levelOrder(root):
    #populate values
    level_order(root,1)

    #print out values in specified format
    output = ""
    for level in values:
        for value in level:
            output += "%d " % value

    print(output[:-1])

