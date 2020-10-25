# Charlie Miller
# Leetcode - 1510. Stone Game IV
# https://leetcode.com/problems/stone-game-iv/

"""
Dynamic programming approach. Go over all possible
moves (just squares). If ANY of the resulting games
aka how many are left for the other player are in a state
where it's impossible to win, then it IS possible for
the current player to win. Also when the game is a square,
it's a guaranteed win
Space: O(n), though can be optimized to O(sqrt(n))
Time: O(n*sqrt(n))
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #previous answers according to n. Add an initial state
        #according to the rules of the game
        possibles = [False] * max(n,2)
        possibles[1-1] = True
        possibles[2-1] = False
        
        for i in range(2,n):
            #adjust i so it reflects how many rocks are in the game
            cur_game = i+1
            
            #case: if it's a sq number, it's a guaranteed win
            if math.sqrt(cur_game).is_integer():
                possibles[i] = True
                continue
                
            #go over every square number under our current number
            cur_base = 1
            cur_sq = cur_base**2
            while cur_sq < i:
                #if any resulting games are impossible for the other player
                #then it IS possible for us
                result_game = cur_game - cur_sq
                if not possibles[result_game-1]:
                    possibles[i] = True
                    break
                    
                cur_base += 1
                cur_sq = cur_base ** 2
                
        return possibles[n-1]
