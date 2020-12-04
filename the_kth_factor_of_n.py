# Charlie Miller
# Leetcode - 1492. The kth Factor of n
# https://leetcode.com/problems/the-kth-factor-of-n/
# Written 2020-12-04

"""
Find all the factors of n. Sort the factors, then
return the element at k-1 if it exists. Else -1
To find all factors, find the modulo of every number
leading up to the square root of that number. Any
that has a mod of 0 is a factor, along with its 
division counterpart
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        #n and 1 are already factors
        factors = [1,n]
        
        #add the square root once only, if it is a
        #square number
        root = math.sqrt(n)
        if root.is_integer():
            factors.append(int(root))
            
        #for every number leading up to the root, see if it's a factor
        for factor in range(2,math.ceil(root)):
            if n % factor == 0:
                factors.append(factor)
                #the division counterpart is also a factor
                factors.append(n//factor)
                
        #sort to give the correct k
        factors.sort()
        
        if len(factors) < k:
            return -1
        
        #factors array is 0 indexed
        return factors[k-1]
        