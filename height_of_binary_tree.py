# Charlie Miller
# Hackerrank - Tree height of a binary tree
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem


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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

"""
recursively traverse thru tree, keeping track of number of recursions
return the largest height from either child
"""

def get_height(root,cur_height):
    #just return recursions here when there's no child
    if not root:
        return cur_height

    #get heights from either child. When we traverse, height increases by 1
    left = get_height(root.left,cur_height+1)
    right = get_height(root.right,cur_height+1)

    return max(left,right)

def height(root):
    root_height = get_height(root,0)

    #problem asks height starting after root, so we subtract 1
    return root_height-1


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
