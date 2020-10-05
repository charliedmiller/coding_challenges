# Charlie Miller
# Leetcode - 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/
    
"""
Sort the intervals by starting point. In cases of ties,
larger intervals should come first (larger ending points)
Compare each interval with each other, though skip those
that fall out of each other. Skip intervals we deemed to
remove already (any that appear in this must already have
been removed) Count number of intervals that haven't been
removed
Time: O(n^2) Space: O(n)
"""

from functools import cmp_to_key
class Solution:
    def interval_cmp(self,a,b):
        #sort by starting interval
        diff = a[0] - b[0]
        
        if diff != 0:
            return diff
        
        #favor larger intervals first (larger end)
        return b[1] - a[1]
    
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #sort intervals
        intervals.sort(key=cmp_to_key(self.interval_cmp))
        
        #keep track of which intervals were removed
        removed = [False] * len(intervals)
        
        #two intervals: current and other. Current should always start on the left
        for i in range(len(intervals)-1):
            #optimization: if it's already been removed, everything else in it 
            #already has been removed, no need  to go over it
            if removed[i]:
                continue
                
            current = intervals[i]
            for j in range(i+1,len(intervals)):
                other = intervals[j]
                
                #Optimization: intervals that start after current intervals' end
                #point are guaranteed not to be within, same with all subsequent
                if other[0] > current[1]:
                    break
                    
                #Optimization, no need to compare if it's already removed
                if removed[j]:
                    continue
                    
                #see if it falls within. We know other always starts after current
                if other[1] <= current[1]:
                    removed[j] = True
                    
        return removed.count(False)
                