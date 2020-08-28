# Charlie Miller
# Leetcode - 470. Implement Rand10() Using Rand7()
# https://leetcode.com/problems/implement-rand10-using-rand7/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        """
        Adding the result of two calls does not give a uniform distribution
        e.g 5 has many ways of getting rolled while 10 only has 1
        If we reduce this to coinflips, we create a binary number based on
        4 flips, then take values 10 and under, otherwise reroll. Generalize this
        to two rand7 calls, where now we build a base 7 number - max 48. We can modulo
        10, but reroll if the base 7 number is over 40, since there would be an uneven
        distribution of numbers
        """
        
        #build base 7 number. Reroll if it's over 
        base7_num = float("inf")
        while base7_num > 39:
            msd = rand7() - 1
            lsd = rand7() - 1

            base7_num = msd * 7 + lsd
            
        #mod to get only 0 - 9
        result = base7_num % 10
        
        #shift result 1 over for the problem
        return result +1
        