# Charlie Miller
# Leetcode - 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

"""
Calculate slope & offset (linear equation) with the first 2 coordinates
Check to see if the equation acurrately predicts the y coordinate for
the rest of the coordinate. I any don't, it's not a straight line
"""

class Solution:
    def check_vertical_line(self,coordinates):
        #in this case, all x coordinates must be the same
        x = coordinates[0][0]
        for coordinate in coordinates:
            if x != coordinate[0]:
                return False
            
        return True
    
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #edge case: a straight line can always be made with 1 coordinate
        if len(coordinates) <= 2:
            return True
        
        #unpack to determine linear eq
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        
        #edge case: it's a vertical line, check differently for this
        if x1 == x2:
            return self.check_vertical_line(coordinates)
        
        #calculate linear equation
        rate = (y2 - y1)/(x2 - x1)
        #determine offset
        dummy_y = rate * x1
        offset = y1 - dummy_y
        
        #check if all other coordinates follow the linear eq
        for coordinate in coordinates:
            expected_y = coordinate[0] * rate + offset
            
            #since dealing with floats, diff might be very low instead of 0
            diff = abs(expected_y - coordinate[1])
            if diff > 0.0000001:
                return False
            
        return True

        
        