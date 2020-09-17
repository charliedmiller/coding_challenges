# Charlie Miller
# Leetcode - 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

"""
Strapped for time, though code is pretty self explanitory
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        string = list(S)
        for char in S:
            if char.isalpha():
                stack.append(char)
                
                
        for i in range(len(S)):
            if string[i].isalpha():
                string[i] = stack.pop()
        
        return ''.join(string)