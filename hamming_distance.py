# Charlie Miller
# Leetcode - 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/
# Written 2020-07-05

"""
Count how many bits show up as 1 in an
XOR of both numbers
"""

class Solution:
    def count_1_bits(self,binary):
        cur_num = binary
        onebits = 0
        while(cur_num != 0):
            #add 1 if the current lsb is 1
            cur_bit = cur_num & 1
            onebits += cur_bit
            #shift right to get next bit
            cur_num >>= 1
            
        return onebits
    def hammingDistance(self, x: int, y: int) -> int:
        #get a number representing all places where
        #there are different bits
        diff_bits = x ^ y
        return self.count_1_bits(diff_bits)