# Charlie Miller
# Leetcode - 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Written 4/21/2020

"""
Record all values for half of the list. 
Then traverse the rest of the list,
comparing each value with the corresponding recorded
list value. Only return true if full list is exhausted
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Set up a fast (2x) pointer so the slow pointer is 
        #guaranteed to be in the middle of the list when the
        #fast pointer completes
        slow_ptr = head
        fast_ptr = head
        #also record values seen by the slow ptr
        values = []
        #Keept track of seen nodes to account for even/odd cases
        num_nodes = 0
        while(fast_ptr is not None):
            num_nodes += 1
            values.append(slow_ptr.val)
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
            if fast_ptr is not None:
                num_nodes += 1
                fast_ptr = fast_ptr.next
                
        #if odd amt elements, the middle will not matter
        if num_nodes % 2 == 1:
            values.pop()

        #do any of the corresponding values not match
        while(slow_ptr is not None):
            next_val = values.pop()
            #no match! not a palindrome
            if slow_ptr.val != next_val:
                return False
            slow_ptr = slow_ptr.next

        return True
            