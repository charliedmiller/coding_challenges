# Charlie Miller
# Leetcode - 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def get_freqs(self,string):
        freqs = defaultdict(int)
        
        for char in string:
            freqs[char] += 1
            
        return freqs
    
    def longestPalindrome(self, s: str) -> int:
        """
        Obtain the frequencies of each letter
        Add the frequencies, but floor'd to nearest even number
        Add one if we do encounter an odd number
        """
        freqs = self.get_freqs(s)

        #init total length, and number if there's an odd "hay" = "there is"
        length = 0
        hay_odd = 0
        
        for freq in freqs.values():
            #encountered odd so we'll add 1 at the end
            if freq % 2 == 1:
                hay_odd = 1
                
            #add frequency floored to nearest even number
            length += (freq//2) * 2
            
        #Add 1 if encountered an odd
        length += hay_odd
        
        return length