# Charlie Miller
# Leetcode - 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Written 2021-01-23

"""
Several checks:
1) each string must have the same set of unique characters
2) each string must match the number of frequencies for their characters
Though the characters for the frequencies don't need to be the same. 
Example: "abbccdddd" has the frequencies 1,2,2,4. It would be close to
"aabbccccd" because it also has the frequencies 1,2,2,4. Here we call it
a meta_frequency
"""

class Solution:
    def get_freqs(self,string):
        """
        Get the frequencies of the characters that appear in the string
        """
        freqs = defaultdict(int)
        
        for char in string:
            freqs[char] += 1
            
        return freqs
    
    def get_meta_freqs(self,freqs):
        """
        Determine the frequency for each frequency
        """
        meta_freqs = defaultdict(int)
        
        for freq in freqs.values():
            meta_freqs[freq] += 1
            
        return meta_freqs
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        #get frequency and meta_frequency for each word
        freqs1 = self.get_freqs(word1)
        freqs2 = self.get_freqs(word2)
        
        meta_freq1 = self.get_meta_freqs(freqs1)
        meta_freq2 = self.get_meta_freqs(freqs2)
        
        #make sure each word uses the same set of characters
        for char in freqs1.keys():
            if char not in freqs2:
                return False
            
            del freqs2[char]

        #make sure freqs1 isn't just a subset of freqs2
        if len(freqs2) != 0:
            return False
        
        #the frequency, and meta_frequencies for both words must match
        for freq,meta_freq in meta_freq1.items():
            if freq not in meta_freq2:
                return False
            
            if meta_freq2[freq] != meta_freq:
                return False
            
            del meta_freq2[freq]
        
        #again make sure meta_freq1 isn't a subset of meta_freq2
        return len(meta_freq2) == 0