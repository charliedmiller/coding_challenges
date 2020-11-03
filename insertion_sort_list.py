# Charlie Miller
# Leetcode - 147. Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/

"""
This implementation sorts in-place, and swaps nodes, not values
maintain 4 pointers: 1 for the insert node - the node we are 
"inserting" for the sort, and 1 for what we're comparing, and
both's respective previous. compare the insert node with the
compare node and previous to determine if node should be inserted there
if so rearrange the necessary pointers and advance insert node, otherwise
advance compare node
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        insert_prev = None
        insert_node = head
        #we can only insert into a "sorted set" which is as long
        #as how many we've sorted so far
        sorted_ct = 0
        while insert_node:
            #compare nodes init
            prev = None
            cur_node = head
            for _ in range(sorted_ct):
                #insert node should be first
                if not prev and insert_node.val <= cur_node.val :
                    temp_next_insert = insert_node.next
                    insert_node.next = head
                    #make insert node head
                    head = insert_node
                    if insert_prev:
                        insert_prev.next = temp_next_insert
                    
                    #make insert node it's prev so it advances correctly
                    insert_node = insert_prev
                    break
                
                elif prev and prev.val < insert_node.val and insert_node.val <= cur_node.val:
                    temp_next_insert = insert_node.next
                    insert_node.next = cur_node
                    prev.next = insert_node
                    if insert_prev:
                        insert_prev.next = temp_next_insert
                        
                    #make insert node it's prev so it advances correctly
                    insert_node = insert_prev
                    break
                    
                #advance compare nodes
                prev = cur_node
                cur_node = cur_node.next
            
            #advance insert node
            insert_prev = insert_node
            insert_node = insert_node.next
            sorted_ct += 1
                
        return head