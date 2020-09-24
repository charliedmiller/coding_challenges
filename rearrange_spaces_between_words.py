# Charlie Miller
# Leetcode - 1592. Rearrange Spaces Between Words
# https://leetcode.com/problems/rearrange-spaces-between-words/

"""
Split into a word array, count the spaces,
distribute evenly to full integer spaces
find out how many remainders there are, give the 
remainders to the rest
"""

class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        words = text.split()
        
        #count the spaces
        for char in text:
            if char == " ":
                spaces += 1
        
        #edge case: there's only 1 word - so append all spaces at the end
        if len(words) == 1:
            result = words[0] + (" " * spaces)
            return result
        
        #how many places to fill spaces
        betweens = len(words)-1
        
        #how many spaces to put in those places
        spc_per_btw = spaces//betweens
        
        #get the remainder
        remainders = spaces - (spc_per_btw * betweens)
        
        #join the words together
        joiner = " " * spc_per_btw
        result = joiner.join(words)
        
        #put remainders at the end
        result += " " * remainders
        return result
        
        
        