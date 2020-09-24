# Charlie Miller
# Leetcode - 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

"""
find the frequencies of each character in each string
for each frequency in t, compare it with that of s
if there's more in t, then that's the added character
"""

class Solution:
    #frequencies of each character
    def get_freqs(self,string):
        #defaultdict for easier new key gen
        freqs = defaultdict(int)
        
        for char in string:
            freqs[char] += 1
            
        return freqs
    
    def findTheDifference(self, s: str, t: str) -> str:
        #get the frequenceis of characters for both strings
        s_freqs = self.get_freqs(s)    
        t_freqs = self.get_freqs(t)
        
        #find the difference btw each character count in both strings
        for char,freq in t_freqs.items():
            
            #when there's more in t, that's the character
            #ok to do it this way bc of defaultdict
            diff = s_freqs[char] - freq
            if diff < 0:
                return char
            
        #edge case: there's no added character
        return ""