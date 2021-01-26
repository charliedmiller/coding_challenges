# Charlie Miller
# Leetcode - 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# Written 2021-01-25

"""
Maintain a min heap that has the k largest items. Only add to it
if a number larger than the min is found, and then pop the min.
Better than just sorting it since it takes n*lg(k) time rather than n*lg(n) time
"""

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #initialize heap
        heap = nums[:k]
        heapq.heapify(heap)
        
        #iterate thru the rest, maintaining a heap of the k highest seen
        for num in nums[k:]:
            if num > heap[0]:
                #add the new number and also pop the min
                heapq.heappushpop(heap,num)
                
        return heap[0]