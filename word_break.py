# Charlie Miller
# Leetcode - 139. Word Break
# https://leetcode.com/problems/word-break/

"""
Select a substring starting from the left. If it's a word,
cut off the remaining and call word-break again. Base case
is when the entire string is a word. Keep trying for each
substring starting from left. Return false if exhaused all
substrings. 
Keep a memo of previous words
"""


class Solution:
    def word_break(self,string):
        
        #base case: whole string is a word
        if string in self.words:
            return True
        
        #split string into words from left, recurse if a word is found
        for end in range(1,len(string)):
            #current word
            cand = string[:end]
            
            if cand not in self.words:
                continue
            
            #we found a word, now recurse
            if self.wb_memo(string[end:]):
                return True
            
        #all substrings exhausted cannot be made
        return False
        
    #wrap all calls of word_break with this. Store answers in a memo
    # if not already found in the memo
    def wb_memo(self,string):
        if string in self.memo:
            return self.memo[string]
        
        ans = self.word_break(string)
        self.memo[string] = ans
        return ans
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #create a memo
        self.memo = {}
        
        #hashify dictionary for faster checks in the dictionary
        self.words = set(wordDict)
        
        return self.wb_memo(s)