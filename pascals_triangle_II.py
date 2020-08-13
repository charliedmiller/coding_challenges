# Charlie Miller
# Leetcode - 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        #calculate all previous rows up to specified index
        #we only need to maintain the previously calculated idx
        #we also only need to calculate half of the row, since it's mirrored
        
        prev = [1]
        ans = []
        max_i = None
        for k in range(1,rowIndex+1):
            size = k+1
            cur = [None for _ in range(size)]
            cur[0] = 1
            
            #up to which index will we calculate the row
            max_i = math.ceil(size/2)
            for i in range(1,max_i):
                cur[i] = prev[i] + prev[i-1]

            #we'll need to calculate +1 cell for rows with even amt cells
            if size % 2 == 0:
                cur[max_i] = cur[max_i-1]
                
            prev = cur
            ans = cur
            
        #for our answer, mirror the array w.r.t. the middle
        for i in range(max_i):
            mi = -(i+1)
            ans[mi] = ans[i]
            
        return ans
        
        