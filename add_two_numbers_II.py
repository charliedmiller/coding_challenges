# Charlie Miller
# Leetcode - 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

"""
build each number separately then add them. Then
build the new list out of this sum
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def build_number(self,root):
        #for every node shift left base 10, then add
        #current node's value to total
        total = 0
        cur_node = root
        while cur_node:
            total *= 10
            total += cur_node.val
            cur_node = cur_node.next
            
        return total
    
    def build_list(self,num):
        #iterate over the digits like a string
        #keep track a previous node to allow for
        # the connection
        num_str = str(num)
        head = ListNode(int(num_str[0]))
        prev = head
        
        for digit in num_str[1:]:
            node = ListNode(int(digit))
            prev.next = node
            prev = node
            
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #get int representations for each number
        num1 = self.build_number(l1)
        num2 = self.build_number(l2)
        #build list for sum of both numbers
        new_list = self.build_list(num1 + num2)
        return new_list