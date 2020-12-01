# Charlie Miller
# Leetcode - 218. The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/
# Written 2020-11-30

"""
Use 2 heaps to keep track of the buildings. 
* 1 min heap to keep track of the right coordinates marking
the end of a building
* 1 max heap to keep track of the tallest building during our scan.
This heap is augmented with a dictionary so we can delete arbitrary
numbers at any time.
Iterate through the buildings. Pop any building ends and process them
before processing the start of this new building. Processing involves
doing the pop (or push) on both heaps, then checking for any changes
in height. If there is a change, mark it in the final bounds list. The
same process is done with pushing to heaps on left ends.
When all buildings have been iterated thru, keep popping and processing the
rest of the buildings that are in both heaps
"""

import heapq

class Heap:
    def __init__(self):
        self.size = 0 #represents DISTINCT numbers
        self.arr = [None]
        self.locations = {}
        self.counts = {}
    
    #get left child index
    def left(self,i):
        left = 2*i
        if not self.valid(left):
            return None
        return left
    
    #get right child index
    def right(self,i):
        right = 2*i + 1
        if not self.valid(right):
            return None
        return right
    
    #get parent index
    def parent(self,i):
        parent = i//2
        if not self.valid(parent):
            return None
        return parent
    
    #return False if there is not such element
    def valid(self,i):
        return self.size >= i
    
    #swap locations of 2 elements
    def swap(self,a,b):
        #be sure to swap the location hashes
        self.locations[self.arr[b]] = a
        self.locations[self.arr[a]] = b
        temp = self.arr[a]
        self.arr[a] = self.arr[b]
        self.arr[b] = temp
    
    def heapify(self,i):
        if not self.valid(i):
            return
        
        #find the larger child
        left_i = self.left(i)
        left_val = float("-inf") if left_i is None else self.arr[left_i]
        right_i = self.right(i)
        right_val = float("-inf") if right_i is None else self.arr[right_i]
        
        larger_child = max(left_val,right_val)
        
        #dont swap if current element is already larger than both
        if self.arr[i] > larger_child:
            return
        
        #swap and heapify with the larger
        if left_val >= right_val:
            self.swap(i,left_i)
            self.heapify(left_i)
        else:
            self.swap(i,right_i)
            self.heapify(right_i)
    
    #insert number
    def push(self,num):
        #only need to increase count if already exists
        if num in self.counts:
            self.counts[num] += 1
            return
        
        #change heap for new number
        self.size += 1
        self.arr.append(num)
        
        #set up all stats for number
        self.counts[num] = 1
        self.locations[num] = self.size
        
        #move number up if necessary
        self.parentify(num)
    
    #move current number up if larger than parent
    def parentify(self,num):
        if num not in self.locations:
            return
        
        cur_i = self.locations[num]
        parent_i = self.parent(cur_i)

        #keep swapping with parent if not root and larger than parent
        while cur_i != 1 and self.arr[parent_i] < num:
            self.swap(cur_i,parent_i)
            cur_i = parent_i
            parent_i = self.parent(cur_i)
        
    #return the top value, and delete it
    def pop(self):
        if not self.valid(1):
            return None
        
        top_val = self.peek()
        self.delete(top_val)
        return top_val
    
    #remove number at arbitrary position
    def delete(self,num):
        if num not in self.locations:
            return
        
        #if more than 1 exists, only need to decrement count
        if self.counts[num] > 1:
            self.counts[num] -= 1
            return
        
        #swap with last in heap, then pop array
        loc = self.locations[num]
        self.swap(loc,self.size)
        self.arr.pop()
        self.size -= 1
        
        #remove stats about number
        del self.locations[num]
        del self.counts[num]
        
        #if element we removed happend to be the last, we're done
        if self.size < loc:
            return
        
        #Maintain heap property with the value that backfilled the
        #position we just deleted
        back_fill = self.arr[loc]
        self.parentify(back_fill)
        loc = self.locations[back_fill]
        self.heapify(loc)
        return
    
    def peek(self):
        return None if self.size == 0 else self.arr[1]


class Solution:
    #process the ends of buildings
    def examine_ends(self,ends,tower_heap,bounds,left):
        prev_end = None
        while ends and ends[0][0] < left:
            #get the current height of the skyline before popping anything
            cur_height = tower_heap.peek()
            #get info about next end and pop height associated with this building
            end_right,end_height = heapq.heappop(ends)
            tower_heap.delete(end_height)
            #see if there's a change in height
            new_height = tower_heap.peek()
            new_height = 0 if new_height is None else new_height
            if new_height != cur_height:
                #in order to have only 1 bound per x coordinate,
                #we have to rewrite the last coordinate if it's also
                #at the same x coordinate as this one
                if prev_end is not None and prev_end == end_right:
                    bounds[-1] = [end_right,new_height]
                else:
                    bounds.append([end_right,new_height])
                prev_end = end_right
        
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ends = []
        bounds = []
        tower_heap = Heap()
        prev_left = None
        for building in buildings:
            left,right,height = building[0],building[1],building[2]
            
            #process the ends of buildings that come before the start
            #of this building
            self.examine_ends(ends,tower_heap,bounds,left)

            #now process start of building
            #take note of current skyline height before processing
            cur_height = tower_heap.peek()
            cur_height = 0 if cur_height is None else cur_height
            
            #push height and end into heaps
            heapq.heappush(ends,(right,height))
            tower_heap.push(height)
            
            #see if the height changed
            new_height = tower_heap.peek()
            if cur_height != new_height:
                #there cannot be 2 bounds of the same x coordinate
                #rewrite the last bound if it has the same x coordinate
                #as this one
                if prev_left is not None and prev_left == left:
                    bounds[-1] = [left,height]
                else:
                    bounds.append([left,height])
                prev_left = left
            
        #process the remaining ends of buildings. 
        #same routine as during the loop conveniently
        self.examine_ends(ends,tower_heap,bounds,float("inf"))
            
        return bounds