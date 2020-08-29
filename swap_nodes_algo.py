# Charlie Miller
# Hackerrank - Swap Nodes [Algo]
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem


#!/bin/python3

import os
import sys
sys.setrecursionlimit(2048)

"""
First build the tree with a simple tree class so it can be easily traversed
Then perform all swaps as the problem describes, easy to know when by using
modulo, and keeping track of current height. Do it post-order to ensure
children are correct, though it probably doesn't matter. inorder traversal
is self explanatory
"""


#
# Complete the swapNodes function below.
#

#simple tree node class for easy traversal
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


#in-order traversal. append after left, but before right
def inorder(root,ans):
    if not root:
        return

    inorder(root.left,ans)
    ans.append(root.val)
    inorder(root.right,ans)
    return ans

def tree_swap(root, k, cur_height):
    if not root:
        return

    #do swaps post-order
    tree_swap(root.left,k,cur_height+1)
    tree_swap(root.right,k,cur_height+1)

    #only perform the swap if our current height is a multiple of k
    if cur_height % k != 0:
        return

    #do the swap
    temp = root.left
    root.left = root.right
    root.right = temp

def swapNodes(indexes, queries):
    #init nodes into our custom node class
    nodes = [Node(idx+1) for idx in range(len(indexes))]

    #assign children according to indexes
    for node,children in enumerate(indexes):
        left = children[0]
        right = children[1]

        #Node doesn't have child when number is -1
        if left != -1:
            nodes[node].left = nodes[left-1]

        if right != -1:
            nodes[node].right = nodes[right-1]


    #perform the swap operations for each "query" (k)
    results = [None] * len(queries)
    for i,k in enumerate(queries):
        tree_swap(nodes[0],k,1)
        results[i] = inorder(nodes[0],[])

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
