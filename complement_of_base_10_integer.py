# Charlie Miller
# Leetcode - 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

"""
We just need to do an XOR with all 1's for the number
Python conveniently represents binary with only the necessary digits
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        #find out how many digits are needed to represent N
        digits = len(bin(N)) - 2
        
        #Create a 1's mask with that many digits
        mask = int(("1" * digits),2)
        
        #do the XOR with the original number
        return N ^ mask