# Charlie Miller
# Leetcode - 593. Valid Square
# https://leetcode.com/problems/valid-square/
# Written 2020-11-11

"""
Find an order of the 4 points that make at least a parallelogram
(4 sides of equal length) Then check the diagonal to satisfy
the square condition
"""

class Solution:
    def has_diagonal(self,base,far_point,side_length_sq):
        #a proper diagonal is c in the equation a^2 + b^2 = c^2
        #the sides are both a and b.
        dist = self.get_dist_sq(base,far_point)
        target_dist = 2*side_length_sq
        return dist == target_dist
    
    def get_dist_sq(self,a,b):
        x_dist = a[0] - b[0]
        y_dist = a[1] - b[1]
        dist_sq = x_dist*x_dist + y_dist*y_dist
        return dist_sq
    
    def square_from_2lines(self,line1A,line1B,line_dist,line2A,line2B):
        
        #make sure third line is same dist as the rest
        third_line = self.get_dist_sq(line1A,line2A)
        if third_line != line_dist:
            return False

        #we've selected 4th line by elim. make sure it has same dist
        fourth_line = self.get_dist_sq(line1B,line2B)
        if fourth_line != line_dist:
            return False
        
        #we made a parallelogram - now make sure it has the correct
        #diagonal. We only need to check 1
        return self.has_diagonal(line1A,line2B,line_dist)
    
    def square_from_line_2pts(self,lineA,lineB,points):
        #make a line with the chosen points, and a line with
        #the remaining. See if they have the same length
        line_dist = self.get_dist_sq(lineA,lineB)
        other_dist = self.get_dist_sq(points[0],points[1])
        
        if line_dist != other_dist:
            return False

        #attempt to make a 3rd line between the 2 established lines
        if self.square_from_2lines(lineA,lineB,line_dist,points[0],points[1]):
            return True
        
        #order might be flipped
        if self.square_from_2lines(lineA,lineB,line_dist,points[1],points[0]):
            return True
        
        return False
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1,p2,p3,p4]
        base = p1
        
        #edgecase: each side has a length of zero. Problem
        #specifies a square to have a POSITIVE length side
        for point in points[1:]:
            #we only need to look for 1, since a sq can't
            #have >1 different length sides
            if point == base:
                return False
        
        #create a line with any 2 points
        for first_neighbor in points[1:3]:
            remaining = points[1:]
            remaining.remove(first_neighbor)
            if self.square_from_line_2pts(base,first_neighbor,remaining):
                return True
            
        #exhausted all options    
        return False
            