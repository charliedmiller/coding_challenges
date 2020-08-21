# Charlie Miller
# Leetcode - 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Build array of odds and evens, maintaining encounter order
        return evens, then odds in 1 array
        """
        
        # init arrays
        odds = []
        evens = []
        
        #add each element into either odds or evens based on parity
        for num in A:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
                
        #give evens, then odds
        return evens + odds