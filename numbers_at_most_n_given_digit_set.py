# Charlie Miller
# Leetcode - 902. Numbers At Most N Given Digit Set
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# Written 2020-11-21

"""
There are 2 kinds of numbers in this problem: 
Numbers that have less digits than n,
Numbers that have the same number of digits.
For those that have less, we can choose any of the given digits for each digit.
For all numbers with  digit sizes smaller than n, we can summarize with the
geometric series (x^1 + x^2 ... + x^(n-1)).
For the other group. choose any number below the most significant digit, as the first 
then choose any for the rest. If the most significant digit is also a choice, solve the
same problem, except where n has its most significant digit cut off.
Add both kinds up to give the total
"""

class Solution:
    def geometric_series(self,x,n):
        #edge case: x == 1 (causes zero division!!)
        if x == 1:
            return n+1
        
        #according to finite geometric series formula
        num = (1 - x**(n+1))
        denom = (1-x)
        return num//denom
    
    def same_digit_numbers(self,digits,n):
        #Only 1 way with no n: use nothing
        if not n:
            return 1
        
        total = 0
        msd = int(n[0]) # most significant digit
        #how many of our given digits can be used as the msb?
        num_lower = sum([digit < msd for digit in digits])
        
        #we can use the lower numbers as msd, then for the rest of the digits
        #we can use ANY digit 
        total += num_lower * (len(digits)**(len(n)-1))
        
        #If the msd is here, we only have one choice, then the same problem,
        #but with n's msd cut off
        if msd in digits:
            total += self.same_digit_numbers(digits,n[1:])
            
        return total
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        #make n a string to use for the same digit numbers routine
        n_str = str(n)
        n_digits = len(n_str)
        #we can use geometric sereis to determine how many numbers with less
        #digits than n can be created
        less_digit_combos = self.geometric_series(len(digits),n_digits-1) - 1
        
        #use a different routine to find the rest (numbers with same number of digits as n)
        digit_nums = [int(digit) for digit in digits]
        same_digit_combos = self.same_digit_numbers(digit_nums,n_str)
        return less_digit_combos + same_digit_combos