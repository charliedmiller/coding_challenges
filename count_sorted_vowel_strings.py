# Charlie Miller
# Leetcode - 1641. Count Sorted Vowel Strings
# https://leetcode.com/problems/count-sorted-vowel-strings/
# Written 2020-12-06

"""
Dynamic program approach. Find out how many sort vowel strings
there are of length n-1, if we use each of the available vowels 
available to us, then add it up. When we use a lexicographically
higher letter, we reduce the choices available to us. This will 
affect the subproblems. Base case is n =1, where it's just the
number of choices we have at the moment
"""

class Solution:
    def count_vowel_strings(self,n,choices):
        #do not recalculate if done already
        hashable = (n,choices)
        if hashable in self.dp:
            return self.dp[hashable]

        #base case: n == 1 - we just use all of the choices available
        if n == 1:
            return choices
        
        #sum the number of choices if we use each vowel available
        #each vowel is represented by a number, which also serves 
        #as the number of choices available afterwards if we use it
        total = 0
        for vowel in range(1,choices+1):
            total += self.count_vowel_strings(n-1,vowel)
            
        #save our result
        self.dp[hashable] = total
        return total
            
    def countVowelStrings(self, n: int) -> int:
        self.dp = {}
        #we can extend it to the entire alphabet or beyond if we wish
        return self.count_vowel_strings(n,5)            