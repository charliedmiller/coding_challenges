# Charlie Miller
# Leetcode - 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Written 2021-01-24

"""
Maintain a priority queue for each of the different lists to merge. It will always
show which is the smallest next node for each of the lists to merge. When we pull
from a particular list, also pull the next node into the priority queue, and let
the queue do the rest. Continue with this until all lists have been exhausted
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #egdecase: no lists
        if not lists:
            return None
        
        heap = []
        
        #initialize the heap with the first item in each list
        for i,list_node in enumerate(lists):
            if not list_node:
                continue
                
            #heap is sorted by the value of the node, idx of the list for ties
            #index is also used to indicate what list to pull from next into the heap
            heapq.heappush(heap,(list_node.val,i,list_node))
    
            #advance each list
            lists[i] = list_node.next
            
        #edgecase: each list is empty
        if not heap:
            return None
        
        #initialize the head, which will be what's returned. Then we'll build it
        _,src_list,head = heapq.heappop(heap)
        
        #advance list used to create the head
        lists[src_list] = head.next
        if lists[src_list]:
            heapq.heappush(heap,(lists[src_list].val,src_list,head.next))
            
        #use cur_node to walk thru the built list
        cur_node = head            
            
        while heap:
            node_val,src_list,next_node = heapq.heappop(heap)
            
            #build our result list
            cur_node.next = next_node
            
            #add next node from list if it exists
            if next_node.next:
                lists[src_list] = next_node.next
                heapq.heappush(heap,(next_node.next.val,src_list,next_node.next))
                
            cur_node = cur_node.next
            
        #make sure the last node is cut off
        cur_node.next = None
        
        return head
            