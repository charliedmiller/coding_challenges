# Charlie Miller
# Leetcode - 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

"""
Maintain a stack for all travelling right. Add to it
if the asteroid is travelling right. Pop it if travelling
left, and it's equal or larger than the top of the stack
keep popping if larger until smaller than top or stack exhausted
Add to remainings only if not destroyed. Tack on the remainder of 
the stack once all asteroids gone thru
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_stack = []
        remainings = []
        
        for asteroid in asteroids:
            #add to stack if travelling right
            if asteroid > 0:
                right_stack.append(asteroid)
            else:
                #to compare apples to apples
                ast_mag = abs(asteroid)
                left_destroyed = False
                
                while right_stack:
                    #top is larger, so asteroid is destroyed. Stop here
                    if right_stack[-1] > ast_mag:
                        left_destroyed = True
                        break
                    #current asteroid is larger, destroy the top 
                    elif right_stack[-1] < ast_mag:
                        right_stack.pop()
                    #They're equal, so both top and current asteroid gets destroyed. Stop here
                    else:
                        left_destroyed = True
                        right_stack.pop()
                        break
                        
                #only add if not destroyed
                if not left_destroyed:
                    remainings.append(asteroid)
                    
        #tack on the remaining right travelling astroids
        remainings.extend(right_stack)
        return remainings
            