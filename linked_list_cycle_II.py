# Charlie Miller
# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

"""
First detect if there is a cycle using fast/slow pointer method
Keep 2 pointers: 1 at beginning, and 1 in the cycle. 
Traverse the cycle fully and check to see if any are equal to the
pointer at the beginning. If not, advance pointer at beginning.
Keep doing this until first cycle node is reached
Space: O(1) Time: O(n^2) 
We could use a hash to make both O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #edgecase: there's no list. No cycle here
        if not head:
            return None

        #check if there even is a cycle
        slow = head
        fast = head
        
        while fast:
            if not fast.next:
                return None
            
            fast = fast.next.next
            slow = slow.next
            
            #cycle detected
            if slow == fast:
                break
                
        #while could have terminated bc end of loop
        if not fast:
            return None
        
        #determine size of the circle cycle_base is 
        #guaranteed to be within the cycle
        cycle_base = slow
        cycle_size = 1
        cycle_check = cycle_base.next
        while cycle_check != cycle_base:
            cycle_size += 1
            cycle_check = cycle_check.next
            
        #determine distance to the base. This is to ensure we don't
        #run forever in a wacky case
        to_base = 0
        cycle_check = head
        while cycle_check != cycle_base:
            to_base += 1
            cycle_check = cycle_check.next
            
        # if cycle_size == 1:
        #     return cycle_base
        
        #check each node from beginning if it's in the cycle
        cycle_head = head
        for __ in range(to_base+cycle_size):
            #traverse whole cycle
            cycle_check = cycle_base.next
            for _ in range(cycle_size):
                if cycle_check == cycle_head:
                    return cycle_head
                cycle_check = cycle_check.next

            #head not found in cycle, advance to next
            cycle_head = cycle_head.next
            
        print("Linked list changed while operating on it")
        return None