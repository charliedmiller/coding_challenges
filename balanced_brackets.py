# Charlie Miller
# Hackerrank - Balanced Brackets
# https://www.hackerrank.com/challenges/balanced-brackets/problem


import math
import os
import random
import re
import sys

"""
Maintain a stack of opening brackets - we must close the most recently seen
opener before fulfilling the next, so we only need to check the top of the stack
When we see a mismatch - we can return false
When there's remaining unfulfilled openers, we also return false
"""


def is_balanced(string):
    match_stack = []

    #maintain a map of which bracket belongs to which
    #easy to extend by extending match
    closers = ")}]"
    match = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    #for each char, if it's an opener just add it to the stack
    #if it's a closer, check if it matches, or if there's any
    # openers to pair with. If there's a match, pop off the opener
    for char in string:
        if char in closers:
            if not match_stack or match[char] != match_stack[-1]:
                return False
            match_stack.pop()

        else:
            match_stack.append(char)

    return not match_stack

# Complete the isBalanced function below.
def isBalanced(s):
    #Adapt True and False to YES and NO
    adapt = {
        True:"YES",
        False:"NO"
    }
    result = is_balanced(s)

    return adapt[result]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
