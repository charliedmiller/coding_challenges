# Charlie Miller
# Leetcode - 61. Rotate List
# https://leetcode.com/problems/rotate-list/

"""
this operation is equivalent to snapping the list in 2 at some point,
then swapping their order. We need 3 locations:
The new "last" node after the swap, 
the new "first" node after the swap,
the current last node
make the next of the new last null
make the next of the current last the current head
return the new "first" as the head

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #edge case: no list, so return nothing
        if not head:
            return head
        
        #get length to determine new first location
        cur_node = head
        length = 0
        while cur_node:
            length += 1
            cur_node = cur_node.next
        
        #determine how many rotations are actually necessary - in cases where k > length
        rotations = k % length
        
        #do nothing if all rotations end in our current state
        if rotations == 0:
            return head
        
        #cycle to the new last. everything after it gets rotated to the left of it
        new_last_idx = length - rotations - 1
        
        #get new last node
        cur_node = head
        for _ in range(new_last_idx):
            cur_node = cur_node.next
        new_last_node = cur_node
        
        #get new first, which is just the next one
        cur_node = cur_node.next 
        new_first = cur_node
        
        #get current last node
        while cur_node.next:
            cur_node = cur_node.next
        cur_last = cur_node
        
        #swap pointers
        cur_last.next = head
        new_last_node.next = None
        
        #return new head
        return new_first