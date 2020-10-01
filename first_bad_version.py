# Charlie Miller
# Leetcode - 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

"""
Do a binary search using isBadVersion
we look at a verision (in the middle) and the next one
when they're different, we've found our culprit
when middle is good, we can eliminate all before middle
when middle is bad, we can eliminate all after middle
Time: O(lg(n))
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def find_bad_version(self,start,end):
        #do binary search
        if start == end:
            return start
        
        #calculate middle validity
        mid = start + int((end - start)/2)
        cur_version_invalid = isBadVersion(mid)
        
        #if very next is bad, that's the first bad version
        if cur_version_invalid != isBadVersion(mid+1):
            return mid+1
        
        if cur_version_invalid:
            return self.find_bad_version(start,mid)
        else:
            return self.find_bad_version(mid+1,end)
        
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n is None:
            return None
        return self.find_bad_version(1,n)
            
        