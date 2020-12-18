# Charlie Miller
# Leetcode - 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/
# Written 2020-12-17

"""
Get all the sums of A and B, and all sums of C and D
into 2 sorted arrays. Annotate each sum with a frequency
using a hash to save operations in the target sum search
With the 2 sorted arrays do a target sum search: 1 pointer at
the end of an array, 1 at the start for the other. Add at both
pointers, if below 0, advance lower, if above, decrement higher
Otherwise multiply the freqs
Time: O(n^2)
"""

class Solution:
    def get_sums(self,a,b):
        #get the sorted sums, and their freqs
        sums = defaultdict(int)
        
        for left in a:
            for right in b:
                total = left + right
                sums[total] += 1
                
        sums_sorted = [(tot,freq) for tot,freq in sums.items()]
        sums_sorted.sort()
        return sums_sorted
    
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if len(A) == 0:
            return 0
        
        #obtain the sums and freqs
        total_ways = 0
        AB = self.get_sums(A,B)
        CD = self.get_sums(C,D)
        
        #do a target sum search for all
        left = 0
        right = len(CD) - 1
        max_left = len(AB) -1
        
        #keep at it until either is exhausted
        while left <= max_left and right >= 0:
            #unpack
            AB_val,AB_freq = AB[left]
            CD_val,CD_freq = CD[right]
            
            total = AB_val+ CD_val
            
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                #4 tuple found. Multiply freqs of the sums found
                total_ways += AB_freq * CD_freq
                
                #advance both pointers
                right -= 1
                left += 1
                
        return total_ways