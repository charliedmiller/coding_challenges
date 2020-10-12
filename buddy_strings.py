# Charlie Miller
# Leetcode - 859. Buddy Strings
# https://leetcode.com/problems/buddy-strings/

"""
If they're not same length or don't have the same
character frequencies they can't be buddies
Everything must be in place except 2 characters
They can be the same exact string, but only if
there is a duplicate character in the string
"""

class Solution:
    def get_freqs(self,string):
        freqs = defaultdict(int)
        
        for char in string:
            freqs[char] += 1
            #the string has duplicate characters
            #only relevant if the strings are the same
            if freqs[char] > 1:
                self.has_duplicates = True
                
        return freqs
    
    def buddyStrings(self, A: str, B: str) -> bool:
        #buddies must be same length
        if len(A) != len(B):
            return False
        
        self.has_duplicates = False

        #buddies must have the same character freqeuncies        
        if self.get_freqs(A) != self.get_freqs(B):
            return False
        
        #count how many are out of place
        incorrects = 0
        for a,b in zip(A,B):
            
            if a != b:
                incorrects += 1
                
            #buddies can't have more than 2 out of place
            if incorrects > 2:
                return False
        
        #edgecase: if they are the same exact string, it's only 
        #possible if there are duplicates
        if incorrects == 0:
            return self.has_duplicates    
        
        #we passed all tests
        return True
