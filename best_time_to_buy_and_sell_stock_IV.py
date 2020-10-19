# Charlie Miller
# Leetcode - 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
    
"""
Note: Solution is correct, but can be optimized (hadn't had the time)
Dynamic program:
Recursively choose whether to buy, and whether to sell
depending on if you bought or sold on a previous day
Cut recusion short if buys are all spent
"""
    
class Solution:
    def mp(self,day,buys,last_bought):
        hashable = "%d,%d,%s" % (day,buys,str(last_bought))
        if hashable in self.memo:
            return self.memo[hashable]
        
        result = self.max_profit(day,buys,last_bought)
        self.memo[hashable] = result
        return result
    
    def max_profit(self,day,buys,last_bought):
        
        if day == len(self.prices) -1:
            return 0 if last_bought is None else self.prices[-1] - last_bought
        elif last_bought is None and buys == 0:
            return 0
        elif last_bought is None:
            #decide whether to buy today or not
            buy_today = self.mp(day+1,buys-1,self.prices[day])
            dont_buy = self.mp(day+1,buys,None)
            return max(buy_today,dont_buy)
        else:
            #decide whether to sell today or not
            
            profit = self.prices[day] - last_bought
            #never sell if we're not making a profit!!
            if profit < 0:
                sell_today = float(-inf)
            else:
                sell_today = self.mp(day+1,buys,None) + profit
                
            dont_sell = self.mp(day+1,buys,last_bought)
            return max(sell_today,dont_sell)
        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        self.prices = prices
        self.memo = {}
        
        return self.mp(0,k,None)