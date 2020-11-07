# Charlie Miller
# Leetcode - 1283. Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

"""
There's a maximum divisor, which is the max value of the array
all subsequent divisors will give the same 'result' of the function
described in the problem. The min divisor is 1, given it must be positive
With these bounds, we can do a binary search to get as close to the threshold
as possible.
Space: O(1) Time: O(n*lg(m)) where m is the max element value in the array
"""

class Solution:
    #perform the function described in the problme
    def sum_divide(self,arr,divisor):
        #edgecase: take 0 arg into account in case 0 is brought in for some reason
        if divisor == 0:
            return float("inf")
        
        return sum([math.ceil(num/divisor) for num in arr])
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #define bounds for binary search
        max_divisor = max(nums)
        min_divisor = 1
        
        #optimization - skip binary search if we know
        #what the divisor should be
        if threshold == len(nums):
            return max_divisor
        
        while max_divisor != min_divisor:
            #calculate 'result' with current mid
            mid = min_divisor + ((max_divisor - min_divisor)//2)
            result = self.sum_divide(nums,mid)
            
            if result < threshold:
                max_divisor = mid
            elif result > threshold:
                min_divisor = mid+1
            else:
                #there could be more than 1 divisor that reaches the exact
                #threshold. We want the MINIMUM one (must check prev num)
                prev = self.sum_divide(nums,mid-1)
                if prev != threshold:
                    return mid
                
                max_divisor = mid
            
        return max_divisor