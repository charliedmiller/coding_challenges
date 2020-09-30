# Charlie Miller
# Leetcode - 179. Largest Number
# https://leetcode.com/problems/largest-number/

"""
I had the right idea, though needed to look at the sln to get there
https://leetcode.com/problems/largest-number/solution/
Create a comparator that compares the numbers created by ordering
them differently (a then b or b then a) Sort using this 
"""


from functools import cmp_to_key
class Solution:
    
    #see what the numbers would look like using each order
    def cmp(self,a,b):
        a_first = int(a+b)
        b_first = int(b+a)
        
        #return the LARGER number as less than (before)
        return b_first - a_first
    
    #for edge cases where there are leading zeros
    def remove_leading_zeros(self,string):
        for start in range(len(string)):
            if string[start] != "0":
                return string[start:]
            
        return string[len(string)-1:]
    
    def largestNumber(self, nums: List[int]) -> str:
        stringified = [str(num) for num in nums]
        stringified.sort(key=cmp_to_key(self.cmp))
        whole = ''.join(stringified) 
        return self.remove_leading_zeros(whole)