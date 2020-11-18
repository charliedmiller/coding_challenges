# Charlie Miller
# Leetcode - 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Written 2020-04-22

"""
Sort by starting interval. For each interval, add to final
interval list if a new interval, or the start is further than
all the previous interval's ends. If the start is behind the furthest
reach so far, just change the last interval's end point with the current
intervals end.Keep track of the furthest reach from all prev intervals to 
help decide this
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by starting number
        intervals.sort(key=lambda interval:interval[0])
        final_intervals = []
        #furthest reaching interval end
        cur_reach = float("-inf")
        for interval in intervals:
            if cur_reach < interval[0]:
                #this interval doesn't intersect: add it to the final
                final_intervals.append(interval)
            else:
                #this interval does intersect, change last interval's end if
                #its less than the current interval's end
                final_intervals[-1][1] = max(interval[1],final_intervals[-1][1])
                
            #update furthest reach so far
            cur_reach = max(interval[1],cur_reach)
            
        return final_intervals
        