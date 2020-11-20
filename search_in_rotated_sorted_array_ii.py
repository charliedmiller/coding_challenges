# Charlie Miller
# Leetcode - 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Written 2020-11-20

"""
Use the same binary search approach as the original
1. Find the pivot point with binary search
2. Find desired number with binary search
Duplicates make the run time O(n) (worst case) but
would still be Theta(lg(n)) (average case). So it may
be acceptable to brute force it since that also has a O(n)
time, and is more simple. There are even some cases where
the brute force solution takes less time than the binary search!
"""

class Solution:
    def search_brute_force(self,nums,target):
        return target in nums
    
    #The code here is implemented incorrectly..and it's a Friday
#     def find_pivot(self,nums):
        
#         start = 0
#         end = len(nums)-1
        
#         while start != end:
#             mid = start + (end - start)//2
            
#             if nums[start] == nums[mid] and nums[mid] == nums[end]:
#                 return mid
#             elif nums[mid] > nums[(mid+1)%len(nums)]:
#                 return (mid+1)%len(nums)
#             elif nums[mid] > nums[end]:
#                 start = mid
#             elif nums[start] > nums[mid]:
#                 end = mid
#             else:
#                 return start
                
#         return start
    
#     def search_binary_search(self,nums,target):
#         if not nums:
#             return False
        
#         offset = self.find_pivot(nums)
        
#         start = 0
#         end = len(nums)
        
#         while start != end:
#             mid = start + (end-start)//2
#             mid_offset = (mid + offset) % len(nums)
            
#             if target < nums[mid_offset]:
#                 end = mid
#             elif nums[mid_offset] < target:
#                 start = mid+1
#             else:
#                 return True
            
#         return False
    
    def search(self, nums: List[int], target: int) -> bool:
        return self.search_brute_force(nums,target)
        