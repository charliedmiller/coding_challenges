# Charlie Miller
# Leetcode - 436. Find Right Interval
# https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Sort the intervals by starting points,
        but annotate their original positions
        for each interval, compare following interval's first with current's last
        record first found interval
        Still O(n^2), though optimizied thru sorting, so we don't have to consider
        intervals that start before the current interval
        """
        
        #annotate and sort intervals
        annotated = [(interval,i) for i,interval in enumerate(intervals)]
        annotated.sort(key=lambda a:a[0][0])
        
        #init our answer, defaulting to -1 when none is found
        rights = [-1] * len(intervals)
        
        
        #compare each following interval's _first_ with current interval's _last_
        #if it fullfills the conditions, use the annotated indexes to fill in
        #the current interval's answer
        for i, cur_annotated in enumerate(annotated):
            interval, orig_idx = cur_annotated[0], cur_annotated[1]
            orig_last = interval[1]
            
            #only compare intervals after our current since we know none start at the
            #same point, and only intervals that start after current can fulfill
            #required conditions
            for candidate,cand_idx in annotated[i+1:]:
                cand_first = candidate[0]
                
                if orig_last <= cand_first:
                    rights[orig_idx] = cand_idx
                    break
                    
        return rights