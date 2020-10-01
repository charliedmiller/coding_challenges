# Charlie Miller
# Leetcode - 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

"""
Solved on 4/18/2020
Find the frequencies and first ocurrence (spelled wrong I know lol) for each
character in string
Iterate over frequencies, do not consider those with frequencies more than 1
find that with the lowest first ocurrance
"""

class Solution:
    #find frequencies, and first ocurrence of each character in string
    def freqs_and_1st_ocurrance(self,string):
        first_ocurrance = {}
        freqs = {}
        
        for i,char in enumerate(string):
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
                first_ocurrance[char] = i
                
        return freqs,first_ocurrance
            
    def firstUniqChar(self, s: str) -> int:
        freqs,first_ocurrance = self.freqs_and_1st_ocurrance(s)
        
        #iterate over frequencies, find that with the smallest first ocurrence
        earliest_idx = float("inf")
        for char,freq in freqs.items():
            #do not consider non-unique characters
            if freq > 1:
                continue
                
            ocurrance = first_ocurrance[char]
            earliest_idx = min(ocurrance,earliest_idx)
            
        #edge case: no unique characters, so return -1
        if earliest_idx == float("inf"):
            earliest_idx = -1
            
        return earliest_idx
        