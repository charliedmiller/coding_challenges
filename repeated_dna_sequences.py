# Charlie Miller
# Leetcode - 187. Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/

"""
maintain a 10 character window for sequences with a queue
Add 1 to a dict for each sequence encountered
Filter out all sequences that appear less than twice
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #edge case: there are no 10 character long sequences
        if len(s) < 10:
            return []
        
        #init window
        window = list(s[:10])
        sequences = defaultdict(int) 
        sequences[''.join(window)] += 1
        
        # Go thru every other sequence
        for char in s[10:]:
            window.pop(0)
            window.append(char)
            
            sequences[''.join(window)] += 1
            
        #filter out any sequences with less than 2
        result = [seq for seq,freq in sequences.items() if freq > 1]
            
        return result
        