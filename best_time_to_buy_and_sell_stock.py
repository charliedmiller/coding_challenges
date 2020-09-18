# Charlie Miller
# Leetcode - 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
A classic problem. I just remember the solution from reading it many times. A great explanation
can be found here: https://www.interviewcake.com/question/python3/stock-price
Short explanation - we keep track of the minimum stock price seen so far, and compare it with
the current day's price. The largest difference between that min, and the current day's price
will be the largest possible profit. When prices only go down, min so far will always be the 
current days price, and profit will always be 0. This emulates not buying at all since buying 
will always result in losses.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #initialize profits to 0
        max_profit = 0
        
        #when there's no prices, we can't do anything so it's 0
        if not prices:
            return max_profit
        
        #can't sell first day, min seen will initialize to first day's value
        min_seen = prices[0]
        
        
        for price in prices:
            min_seen = min(min_seen,price)
    
            #calc profit if we sell today, buying on the day the minimum has been seen
            profit = price - min_seen
            max_profit = max(max_profit,profit)
            
        return max_profit
            