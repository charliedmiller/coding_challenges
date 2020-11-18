# Charlie Miller
# Leetcode - 858. Mirror Reflection
# https://leetcode.com/problems/mirror-reflection/
# Written 2020-11-17

"""
We can imagine the room to actually be a square in a repeating 
grid. The corners of each square has the sensors. If we project
the laser in this grid in a STRAIGHT line, which point will it 
reach first? 

Q__0__Q ...
|  |  |
2__1__2 ...
|  |  |
Q__0__Q ...

This depends on the proportion of p to q. For every
p we go up some distance q. When will the laser line up with a corner?
To find this we need to simplify the proportion - this will tell us
the horizontal, and vertical distance traveled by the laser before 
reaching the corner. There are 4 possible orientations the intersection 
could be - use the vert and horiz distances to find out which. Then
use that to tell which sensor was hit
"""

class Solution:
    def get_divisors(self,num):
        #each divisor is in a pair where the smaller is equal
        #or smaller to the square root of the number. Find
        #all those numbers, then add its counter-part
        divisors = []
        #get sqrt separatly if the number is square
        num_sqrt = math.sqrt(num)
        if num_sqrt.is_integer():
            divisors.append(int(num_sqrt))
            
        for i in range(2,math.ceil(num_sqrt)):
            #found a divisor, add it and its counterpart
            if num % i == 0:
                divisors.append(i)
                divisors.append(num//i)
                
        #add 1 and the number itself
        divisors = [num] + divisors + [1]
        return divisors
    
    def greatest_common_divisor(self,larger,smaller):
        #gcd candidates are only divisors of the smaller number
        candidates = self.get_divisors(smaller)
        candidates.sort(reverse=True)
        
        #return largest found candidate
        for cand in candidates:
            if larger % cand == 0:
                return cand
            
        return 1
        
    def mirrorReflection(self, p: int, q: int) -> int:
        #simplify the ratio - divide by gcd
        gcd = self.greatest_common_divisor(p,q)
        #dividing by gcd tells the horizontal and vertical distance traveled
        horizontal_dist = p//gcd
        vertical_dist = q//gcd
        
        #what is at the top right corner according to the layout orientation
        #  Q_(0)(Q)
        #  |  |  |
        #  2_(1)(2)
        #  |  |  |
        #  Q__0__Q
        #
        #1 means flipped. rows is vertical, cols is horizontal
        layouts_tr = [[1,2],
                      [0,-1]]

        #mod by 2 because each orientation has a period of 2 (periodic)
        #add 1 because layouts_tr is 0 indexed
        vert_orientation = (vertical_dist+1)%2
        horiz_orientation = (horizontal_dist+1)%2
        
        #get the sensor at the top right according to orientation where
        #laser intersected with a corner
        sensor = layouts_tr[vert_orientation][horiz_orientation]
        return sensor