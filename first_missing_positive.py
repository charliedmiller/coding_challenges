# Charlie Miller
# Leetcode - 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

"""
Note: Problem calls for O(1) space, but permits using the array
itself as storage thru a hint - kind of a cheat since ordinarily 
you shouldn't modify the input...
2 passes:
1) swap elements so they follow 1,2,3... from the beginning. Do not
advance index if we do a swap. Advance index when we see a negative,
duplicate, or number above possible range (above n)
2) numbers should be in order from beginning, find any unexpected
if everything's expected, the next number is the "missing" positive
"""

class Solution:
    def swap(self,arr,a,b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
        
    def firstMissingPositive(self, nums: List[int]) -> int:
        #swap elements in array so they're in positive number order
        i = 0
        while i < len(nums):
            num = nums[i]
            #advance if it's a number we're not looking for
            if num <= 0 or num > len(nums) or num == nums[num-1]:
                i += 1
            else:
                #we found a number, swap it into the correct place
                self.swap(nums,num-1,i)
                #do NOT advance since now we're examining a new number
                
        #walk thru array execting 1,2,3...
        for i,num in enumerate(nums):
            expected = i+1
            if num != expected:
                return expected
            
        #array's been exhausted, so it must be the very next number
        return len(nums)+1