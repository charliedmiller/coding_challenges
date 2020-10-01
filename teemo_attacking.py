# Charlie Miller
# Leetcode - 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/

"""
For each interval, poisoned time will be the smaller of
the default duration, or the interval size. Accumulate time.
For the last time, it will always be the duration
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        #edge case , there are no times, so poisoned time is 0
        if not timeSeries:
            return 0
        
        total_time = 0
        
        # keep track of previous time to determine interval size
        prev_time = timeSeries[0]
        for time in timeSeries[1:]:
            #add min of duration or interval size
            total_time += min(duration,time - prev_time)
            prev_time = time

        #add duration for the last time (there is no interval)
        total_time += duration
        
        return total_time