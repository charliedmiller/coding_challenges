# Charlie Miller
# Leetcode - 47. Permutations II
# https://leetcode.com/problems/permutations-ii/
# Written 2020-11-12

"""
Create the permutation list as if there were no duplicates
Put the whole list of permutations in a hash set to remove duplicate
sequences
convert back to list of lists
----------
How to create a full permutation list:
choose 1 element from list as first in sequence
find the all permutations for all others in the list, 
then append to the right of the chosen first element
do this for each element and combine to master list. 
"""

class Solution:
    def permute_unique(self,seq):
        #permutations of nothing is just 1 emptyset
        if not seq:
            return [[]]
        
        #save results for later. Bc duplicates, we're likely to see
        #calls with the same sequence again
        hashable = str(seq)
        if hashable in self.memo:
            return self.memo[hashable]
        
        #master list of permutations
        cur_permutations = []
        for i,num in enumerate(seq):
            #left (num) has been selected. Get permutations made from the rest
            right_permutations = self.permute_unique(seq[:i]+seq[i+1:])    
            
            #for each permutation, add our chosen left, and add it to the left
            #then add the resulting seq to our master list
            for right_permutation in right_permutations:
                cur_permutations.append([num] + right_permutation)
        
        #save result for future calls
        self.memo[hashable] = cur_permutations
        return cur_permutations
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.memo = {}
        #we're more likely to get duplicate memo-ized calls if we sort the list
        nums.sort()
        #get permutations, with duplicates
        permutations = self.permute_unique(nums)
        
        #remove duplicates, first we have to make each sequence hashable
        permutations = [tuple(permutation) for permutation in permutations]
        permutations = list(set(permutations))
        permutations = [list(permutation) for permutation in permutations]
        
        return permutations