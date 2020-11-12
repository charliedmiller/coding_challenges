# Charlie Miller
# Leetcode - 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/
# Written 2020-11-10

"""
Flip the row, then invert the value in a list comp
"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = [[px^1 for px in row[::-1]] for row in A]
        return result