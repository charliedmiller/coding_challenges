# Charlie Miller
# Leetcode - 688. Knight Probability in Chessboard
# https://leetcode.com/problems/knight-probability-in-chessboard/

"""
Calculate probability of landing on chessboard for each position,
for each move lower than K recursively. Sum the probabilities
for each move and divide by 8 since each move is equally probable
(Strapped for time for more comments)
"""

class Solution:
    def valid(self,x,y):
        if x < 0 or y < 0:
            return False
        
        if x > self.max_x or y > self.max_y:
            return False
        
        return True
    
    def knight_probability(self,x,y,K):
        if not self.valid(x,y):
            return 0
        
        if K == -1:
            return 1
        
        if self.dp[x][y][K]:
            return self.dp[x][y][K]
        
        #next move positions
        positions = [(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x-2,y+1),(x-2,y-1)]
        total_prob = 0
        for mx,my in positions:
            total_prob += self.knight_probability(mx,my,K-1)

        ans = total_prob/8
            
        self.dp[x][y][K] = ans
        return ans
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        self.dp = [[[None for _ in range(K)] for __ in range(N)] for ___ in range(N)]
        self.max_x = N-1
        self.max_y = N-1
        
        return self.knight_probability(c,r,K-1)
        
                   
                   