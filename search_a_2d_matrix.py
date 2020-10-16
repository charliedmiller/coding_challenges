# Charlie Miller
# Leetcode - 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

"""
Do 2 binary searches. With the given properties
we can take some shortcuts
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #edgecase: no matrix is provided
        if not matrix:
            return False
    
    
        if not matrix[0]:
            return False
        
        #first search the row
        start = 0
        end = len(matrix)
        row = None
        
        while start != end:
            mid = start + (end-start)//2
            row = mid
            value = matrix[mid][0]
            #we found our target already
            if value == target:
                return True
            #target is before our current row
            elif value > target:
                end = mid
            else:
                #target COULD be in our row. Check for that and break if so
                #otherwise continue searching
                if mid == len(matrix)-1 or matrix[mid+1][0] > target:
                    break
                else:
                    start = mid+1
        
        #optimization: if target is lower than top left or 
        #target is higher than bottom right we know it won't be there
        if row == 0 and target < matrix[0][0]:
            return False
        
        if row == len(matrix)-1 and target > matrix[-1][-1]:
            return False
        
        #search the row
        start = 0
        end = len(matrix[row])
        
        while start != end:
            mid = start + (end-start)//2
            value = matrix[row][mid]
            
            if target < value:
                end = mid
            elif target > value:
                start = mid+1
            else:
                return True
            
        #exhausted our search - it's not here
        return False
                    