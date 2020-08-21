# Charlie Miller
#Leetcode - 143 Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        3 passes:
        1) Get a reference to each node in order into an array
        2) with 2 pointers at the end and beginning, swap the .next's of the 2 nodes
            -Advance the pointers closer to eachother until they pass one another
        3) Knowing the size of our list, advance to the end and make sure the last node has 
           null as next
        
        """
        
        if not head:
            return None
    
        # init ordered reference array
        list_arr = []
        cur_node = head
        
        # populate reference array
        while cur_node:
            list_arr.append(cur_node)
            cur_node = cur_node.next
            
        # init left right pass
        size = len(list_arr)
        left = 0
        right = size - 1
        
        # swap pointers of left and right
        while left < right:
            temp = list_arr[left].next
            list_arr[left].next = list_arr[right]
            
            # do not assign right's pointer if indicies are right next to each other
            if left+1 < right:
                list_arr[right].next = temp
                
            #advance indicies
            left += 1
            right -= 1
            
        # Advance to what we know as the end node and make the .next node None
        cur_node = list_arr[0]
        for _ in range(size-1):
            cur_node = cur_node.next
        cur_node.next = None
        
        return head