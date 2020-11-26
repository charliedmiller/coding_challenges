# Charlie Miller
# Leetcode - 395. Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Written 2020-11-26

"""
Divide and conquer - get the frequency of each character
We know that any char that doesn't make the k minimum can't be
included in the string, so we split the string at all
locations where those chars are found, and we'll run the same
routine with the now split off strings. Base case is where either
all characters acheive the k requirement, or all don't.
"""

class Solution:
    def get_freqs(self,string):
        freqs = defaultdict(int)
        
        for char in string:
            freqs[char] += 1
            
        return freqs
    
    def longestSubstring(self, s: str, k: int) -> int:
        freqs = self.get_freqs(s)
        
        #base case: all characters in the string meet the
        #k requirement
        if all([freq >= k for freq in freqs.values()]):
            return len(s)
        
        #split off the string at locations where there are
        #characters that DONT meet the k requirement
        strings = [s]
        for char,freq in freqs.items():
            #confirm that char doesn't meet k requirement
            if freq >= k:
                continue
            
            #do the splitting
            new_strings = []
            for string in strings:
                #filter out null strings
                next_strings = [ns for ns in string.split(char) if len(ns) > 0]
                new_strings.extend(next_strings)
                
            strings = new_strings
            
        #base case: NONE of the chars meet the k requirement
        if len(strings) == 0:
            return 0
            
        #return the longest found substring that meets the requirement, given the
        #remaining valid strings left
        return max([self.longestSubstring(string,k) for string in strings])
