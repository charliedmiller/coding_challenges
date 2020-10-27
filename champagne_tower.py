# Charlie Miller
# Leetcode - 799. Champagne Tower
# https://leetcode.com/problems/champagne-tower/

"""
Solution is incorrect/too slow. But this is what I wrote for today
"""

class Solution:
    def update_rate(self,x,y,added_rate,new_cups):
        
        self.rates[y][x] += added_rate
        
        if abs(1.0 - self.fills[y][x]) > self.fc:
            return [(x,y)]
            
        if y == 99:
            return []
        
        desc_rate = added_rate/2
        new_cups.extend(self.update_rate(x,y+1,desc_rate,new_cups))
        new_cups.extend(self.update_rate(x+1,y+1,desc_rate,new_cups))
        
        return new_cups

                        
        
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured >= 5050:
            return 1
        
        self.fills = [[0.0 for __ in range(100)] for _ in range(100)]
        self.rates = [[0.0 for __ in range(100)] for _ in range(100)]
        self.filled = [[False for __ in range(100)] for _ in range(100)]
        
        self.fc = 0.00000000001
        self.rates[0][0] = 1.0
        cur_poured = [(0,0)]
        for cup_num in range(poured):
            remaining = 1.0
            
            while remaining > self.fc:
                min_next = min([1-self.fills[y][x] for x,y in cur_poured])
                to_pour = min(min_next,remaining)
                for x,y in cur_poured:
                    self.fills[y][x] += to_pour * self.rates[y][x]
                    
                for x,y in cur_poured[:]:
                    #don't do anything if cup hasn't finished being filled
                    if not (abs(1.0 - self.fills[y][x]) < self.fc):
                        continue
                        
                    self.filled[y][x] = True
                    new_cups = self.update_rate(x,y,self.rates[y][x],[])
                    cur_poured.extend(new_cups)
                    cur_poured.remove((x,y))
                    
                remaining -= to_pour
                
                
        return self.fills[query_row][query_glass]
                        
                