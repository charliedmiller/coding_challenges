# Charlie Miller
# Leetcode - 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Written 2020-04-22

"""
Sort the array descending, then give the kth element.
Future me: can do this with a heap as well
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        idx = k - 1
        return nums[idx]
        