# Charlie Miller
# Leetcode - 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

"""
Consider all combinations recursively, if the sum is greater than the
target, cut off the recursive path early. Do not consider paths with
candidates that come before the current candidate, since they considered
the combos with the current candidate before. When the target is matched,
add it to the combinations
"""


class Solution:
    def combination_sum(self,candidates,cur_combo,target,min_cand):
        #we added too much; cut off here
        if target < 0:
            return
        
        #consider only future candidates (self included)
        i = min_cand
        
        #consider next number to add
        for cand in candidates[min_cand:]:
            #add candidate to the combinations
            cur_combo.append(cand)
            new_target = target - cand
            
            #either we reach the target or we recurse deeper until we do
            if new_target == 0:
                self.combinations.append(cur_combo[:])
            else:
                self.combination_sum(candidates,cur_combo,new_target,i)
                
            #this number no longer needs to be considered
            cur_combo.pop()
            i += 1
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        #adapt to helper function
        self.combination_sum(candidates,[],target,0)
        
        return self.combinations