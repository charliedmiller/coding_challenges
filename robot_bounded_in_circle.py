# Charlie Miller
# Leetcode - 1041. Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/

"""
If the robot remains in a circle, it means the instructions
are periodic. We can check if it's periodic by checking the
robot's position and orientation is the originating position
and orientation after executing it's instructions. Given it can
only go in 4 directions, the max period is 4. So we only need
to execute the instructions 4 times and see if it returns to
the original position/orientation anytime up to 4
"""

class Solution:
    #give next position based on orientation
    def move_forward(self,x,y,o):
        directions = {
            "w":(x-1,y),
            "e":(x+1,y),
            "s":(x,y-1),
            "n":(x,y+1)
        }
        
        return directions[o]
    
    #give next orientation based on orientation
    def turn_left(self,o):
        directions = {
            "w":"s",
            "s":"e",
            "e":"n",
            "n":"w"
        }
        
        return directions[o]
    
    #give next orientation based on orientation
    def turn_right(self,o):
        directions = {
            "w":"n",
            "n":"e",
            "e":"s",
            "s":"w"
        }
        
        return directions[o]
    
    #Execute the instructions, updating orientation and position according to the opcode
    def follow_instructions(self,x,y,o,instructions):
        
        for instruction in instructions:
            if instruction == "G":
                # print(self.move_forward(self.x,self.y,self.o))
                self.x,self.y = self.move_forward(self.x,self.y,self.o)
            elif instruction == "L":
                self.o = self.turn_left(self.o)
            elif instruction == "R":
                self.o = self.turn_right(self.o)
                
                
        
    def isRobotBounded(self, instructions: str) -> bool:
        self.x = 0
        self.y = 0
        self.o = "n"
        #execute instructions 4 times. If at anytime it returns to
        # the original position, we'll know it's periodic, and therefore will stay
        # within a circle
        for i in range(4):
            self.follow_instructions(self.x,self.y,self.o,instructions)
            # print(self.x,self.y,self.o)
            if self.x == 0 and self.y == 0 and self.o == "n":
                return True
        #Instructions are not periodic    
        return False