# Charlie Miller
# Leetcode - 165. Compare version Numbers
# https://leetcode.com/problems/compare-version-numbers/


"""
Split the numbers out by . and compare digits
when one runs out (due to ties) keep examining the remainder for any non-0s
Non-0 implies higher version
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #Split out the digits of the versions
        v1_digits = version1.split(".")
        v2_digits = version2.split(".")
        
        #compare digits until one of them runs out
        while v1_digits and v2_digits:
            v1_digit = int(v1_digits.pop(0))
            v2_digit = int(v2_digits.pop(0))
            
            if v1_digit > v2_digit:
                return 1
            
            if v1_digit < v2_digit:
                return -1
            
        #If both happen to run out then it's a tie
        if not v1_digits and not v2_digits:
            return 0
        
        #Determine which to continue examining, and the result if that one is
        #found to be larger
        if v1_digits:
            remaining = v1_digits
            result_if_larger = 1
        else:
            remaining = v2_digits
            result_if_larger = -1
            
        #empty out the remainder, looking for any non-0s
        while remaining:
            digit = int(remaining.pop(0))
            if digit != 0:
                return result_if_larger
            
        #Despite 1 version having more digits, it's still a tie. As defined by problem, no digit implies 0
        return 0