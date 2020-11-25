# Charlie Miller
# Leetcode - 1015. Smallest Integer Divisible by K
# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Written 2020-11-25

"""
If K ends in an even number or 5, it cannot be done
since the last digit will always be even, or 5 for all
multiples. For all others, there will always be a number,
up to K ones. So we can brute force all numbers of all 1s
from 1 digit to K digits. We can skip those that are below K
"""

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        #last digit cannot be even or 5
        last_digit = int(str(K)[-1])
        if last_digit in [0,2,4,5,6,8]:
            return -1
        
        #iterate thru all numbers of all 1s
        k_len = len(str(K))
        #max will be K digits long
        cycle_high = K+1
        # initialize number to compare to
        number = int("1" * k_len)
        digits = k_len
        while digits < cycle_high:
            if number % K == 0:
                return digits
            
            #increase to next number, and num digits
            number = number * 10 + 1
            digits += 1
            
        return -1
                
        