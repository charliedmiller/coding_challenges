# Charlie Miller
# Leetcode - 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# Written 2020-11-28

"""
Use an augmented max heap to keep track of the maximum of the window. The
heap must be able to delete any arbitray member inside (not just top). When 
this happens, we can heapify at that spot to maintain heap property. Use a 
hash to help locate arbitrary members and delete numbers leaving the window. 
Use a counter hash for each number to keep track of duplicates. 
(I needed to practice my heap implementations)
Time: O(nlg(k)) Space: K
"""

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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        maxes_size = len(nums) - (k-1)
        maxes = [None for _ in range(maxes_size)]
        
        #create window and window heap
        window = nums[:k]
        window_heap = Heap()
        for value in window:
            window_heap.push(value)
        maxes[0] = window_heap.peek()
        
        
        for i,next_num in enumerate(nums[k:]):
            mi = i+1
            #change window to reflect current state
            to_delete = window.pop(0)
            window.append(next_num)
            
            #change heap to reflect current state
            window_heap.delete(to_delete)
            window_heap.push(next_num)
            
            #record max in heap
            maxes[mi] = window_heap.peek()
            
        return maxes
        