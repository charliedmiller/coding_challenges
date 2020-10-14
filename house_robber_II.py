# Charlie Miller
# Leetcode - 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

"""
Same as house robber I, except keep track if
you robbed the first house to calculate the
last one
"""

class Solution:
    def rob_circular(self,houses,i,robbed_prev,robbed_first):
        #get memo result for faster calc
        hashable = str(i) + str(robbed_prev) + str(robbed_first)
        if hashable in self.memo:
            return self.memo[hashable]

        #last house rob only if we can (not when first was robbed)
        if i == len(houses)-1:
            ans = 0
            if not robbed_prev and not robbed_first:
                ans = houses[i]
        
        #we robbed last time so can't rob this time
        elif robbed_prev:
            ans = self.rob_circular(houses,i+1,False,robbed_first)
            
        #decide whether to rob this time. Choose the max of the choices
        else:
            #record if we robbed the first house or not
            rob_first_arg = robbed_first if i != 0 else True
            do_rob = self.rob_circular(houses,i+1,True,rob_first_arg) + houses[i]

            rob_first_arg = robbed_first if i != 0 else False
            dont_rob = self.rob_circular(houses,i+1,False,rob_first_arg)
            
            ans = max(do_rob,dont_rob)
        
        #record into our memo
        self.memo[hashable] = ans
        return ans
    
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        
        return self.rob_circular(nums,0,False,None)