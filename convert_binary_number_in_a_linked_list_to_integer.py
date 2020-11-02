# Charlie Miller
# Leetcode - 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

"""
Maintain a total number. For each new node, bitwise shift left
the total, then add the current node's value. This works like building
a number little endian
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        cur_node = head
        
        while cur_node:
            #shift left
            total <<= 1
            #add cur value
            total += cur_node.val
            #advance node
            cur_node = cur_node.next
            
        return total
        