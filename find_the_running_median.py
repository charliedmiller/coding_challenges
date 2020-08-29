# Charlie Miller
# Hackerrank - Find the Running Median
# https://www.hackerrank.com/challenges/find-the-running-median/problem

#!/bin/python3

import os
import sys
import heapq

"""
Maintain 2 heaps. One max heap for the running lower half of the set
The other a min heap for theupper half. Make sure the heap sizes are 
within 1 of one another. If they're not, do an exchange, popping maxes
from lower, mins from upper until they are. 

return average btw lower max and upper min when there's an even count
return top of the larger when there's an odd count
"""



def runningMedian(a):
    #array for each calcualted median
    medians = [None] * len(a)

    #heaps
    lowers = []
    uppers = []

    for ct,num in enumerate(a):
        #enumerate returns 0 indexed numbers, so must shift by 1
        ct += 1
        
        #insert most recent number into appropriate heap
        #we flip for lowers because python heapq only maintains min heaps
        #flipping effectively allows us to maintain a max heap
        if not lowers or (0-num) > lowers[0]:
            heapq.heappush(lowers,(0-num))
        else:
            heapq.heappush(uppers,num)

        #maintain balance between heaps
        sizes = [(len(arr),arr) for arr in [lowers,uppers]]

        #do not balance if both heaps are of equal size
        if sizes[0][0] != sizes[1][0]:

            smaller = min(sizes)[1]
            bigger = max(sizes)[1]

            #take away from the larger heap until they are within 1 of each other
            while len(bigger) > len(smaller) +1:
                popped = heapq.heappop(bigger)
                #no matter how we exchange, we have to flip the number
                heapq.heappush(smaller,(0-popped))

        #calc average btw lower and upper heap tops when count is even
        if ct % 2 == 0:
            left = (0-lowers[0])
            right = uppers[0]
            ans = (left+right)/2
        #Otherwise median is the top of the larger heap
        else:
            if len(lowers) > len(uppers):
                ans = (0-lowers[0])
            else:
                ans = uppers[0]

        medians[ct-1] = ans

    return medians






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
