# Charlie Miller
# Leetcode - 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

"""
Split out string with python's split, which will take out trailing whitespaces
get the length of the last word
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #Split string
        splitted = s.split()
        
        #if there's no valid words, return 0
        if not splitted:
            return 0
        
        #as specified by problem get the length of the last word
        return len(splitted[-1])