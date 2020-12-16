# Charlie Miller
# Leetcode - 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Written 2020-12-15

"""
To get log(n) time, we need to get the original array sorted by absolute
value in n time. We can do this by partitioning the array by its positives
and negatives. Then do a merge routine to sort by absolute value. No need
to sort the partitions bc they are already sorted. Finally, square each value
in the sorted array
"""

class Solution:
    def merge(self,a,b):
        #init array
        size = len(a)+len(b)
        arr = [None for _ in range(size)]
        
        #set up "sentinel" values for merge
        a.append(float("inf"))
        b.append(float("inf"))
        
        #set up indicies to track the merge
        a_idx = 0
        b_idx = 0
        
        #put into the array whatever is the smaller of the next element
        #in both arrays
        for i in range(size):
            if a[a_idx] < b[b_idx]:
                arr[i] = a[a_idx]
                a_idx += 1
            else:
                arr[i] = b[b_idx]
                b_idx += 1
                
        return arr
        
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #edgecase: no array exists
        if not nums:
            return nums
        
        #determine where to partition the array 
        first_positive = len(nums)
        for i,num in enumerate(nums):
            if num >= 0:
                first_positive = i
                break
        
        if first_positive == 0:
            #edgecase: there are no negatives - negative partition must be empty
            negatives = []
        else:
            #convert negative numbers to positive before merging
            negatives = [0-num for num in nums[first_positive-1::-1]]

            
        positives = nums[first_positive:]
        
        #merge the partitions
        inorder = self.merge(negatives,positives)
        
        #square each element in the merged array
        return [num**2 for num in inorder]