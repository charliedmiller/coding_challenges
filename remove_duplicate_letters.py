# Charlie Miller
# Leetcode - 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

"""
Note:the following algo is correct, but not most efficient. Check out problem
for most efficient solution
Dynamic program: for each character,
choose whether to remove it or not recursively
we cannot remove those that only have 1 ocurrence
we must remove those the already gave a pass on
choose the lexicographically smallest result
"""

class Solution:
    
#     def str_to_value(self,string):
#         value = 0
        
#         for exp,char in enumerate(reversed(string)):
#             to_add = ord(char) * (26 ** exp)
#             value += to_add
            
#         return value
            
        
    #get freqs for each character
    def get_freqs(self,string):
        freqs = defaultdict(int)
        for char in string:
            freqs[char] += 1
            
        return dict(freqs)
    

    #get result if subproblem was encountered before
    #otherwise calculate result then store it
    def rd_memo(self,string,i,freqs):
        #create a hashable for the hash table
        hashable = str(i) + str(freqs)    
        if hashable in self.memo:
            return self.memo[hashable]

        result = self.remove_duplicates(string,i,freqs)
        self.memo[hashable] = result
        return result
    
    def remove_duplicates(self,string,i,freqs):
        #we've spent the entire string, it will always be an empty string
        if i > len(string)-1:
            return ""
        
        
        first_char = string[i]
        
        #only instance of the character or all duplicates already removed
        #we have to use this character
        if first_char not in freqs or freqs[first_char] == 0:
            return first_char + self.rd_memo(string,i+1,freqs)
        #we already kept a previous instance of this char, so we must remove it here
        elif self.kept[first_char]:
            freqs[first_char] -= 1
            ans = self.rd_memo(string,i+1,freqs)
            freqs[first_char] += 1
            return ans
        
        #in all other cases we have a choice to remove or not remove. Calculate both
        #then choose the lex smaller results of the two
        freqs[first_char] -= 1
        remove_result = self.rd_memo(string,i+1,freqs)
        freqs[first_char] += 1
        
        self.kept[first_char] = True
        dont_remove = first_char + self.rd_memo(string,i+1,freqs)
        self.kept[first_char] = False
        
        ans = min(dont_remove,remove_result)
        return ans
        
    
    def removeDuplicateLetters(self, s: str) -> str:
        freqs = self.get_freqs(s)
        #only keep the freqs of the characters we have to remove
        freqs = {char:freq-1 for char,freq in freqs.items() if freq-1 > 0}
        #dict of kept characters
        self.kept = {char:False for char in freqs.keys()}
        # self.lasts = self.last_occurrence(s)
        
        self.memo = {}
        
        smallest = self.remove_duplicates(s,0,freqs)
        return smallest