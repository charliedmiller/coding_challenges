# Charlie Miller
# Leetcode - 382. Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/
# Written 2020-12-02

"""
Find out how many elements are in the linked list during __init__
When getRandom is called, choose a random index [0,size) based on size
Then traverse to that index and return the value
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        #find out how many elements linked list has
        size = 0
        cur_node = head
        while cur_node:
            size += 1
            cur_node = cur_node.next
            
        #record size and head of list
        self.size = size
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        #choose a random index based on size
        idx = randint(0,self.size-1)

        #traverse to that index
        cur_node = self.head
        for _ in range(idx):
            cur_node = cur_node.next
            
        return cur_node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()