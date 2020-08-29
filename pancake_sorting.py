# Charlie Miller
# Leetcode - 969. Pancake Sorting
# https://leetcode.com/problems/pancake-sorting/

"""
Following solution may not give the optimal flip path, though flips will
be max 2n, which is well within the specifications of the problem.
Time complexity: O(nlgn)
Space complexity: O(n)

We observe once a number has been sorted, it never has to be touched again.
Sorting an element requires max 2 flips:
First to bring it to the front
Second to bring it to its correct place.
Once in place, we only need to consider elements that come before it. Repeat
until sorted

"""



class Solution:
    def flip(self,arr,k):
        #record the flip index, then do the flipping
        #k+1 because of an error in the problem description (1 indexed)
        self.flips.append(k+1)
        return arr[:k+1][::-1] + arr[k+1:]
    
    def pancakeSort(self, A: List[int]) -> List[int]:
        self.flips = []
        
        #set up the correct order so we know what element to look for
        #at each sort step. If we knew all elements would be 1..n, this 
        #step wouldn't be required, and whole algo will turn to O(n)
        order = A[:]
        order.sort()
        
        #Working array, and index of array we are sorting
        cur_arr = A
        sorting_idx = len(A) - 1
        
        while sorting_idx > 0:
            #get the next number we need to sort with
            next_num = order[sorting_idx]
            
            #if it's already in place skip this step!
            if cur_arr[sorting_idx] == next_num:
                sorting_idx -= 1
                continue
                
                
            #find location of the next number
            first_flip = cur_arr.index(next_num)
            
            #flip up to location of next number to push number to front
            if first_flip != 0:
                cur_arr = self.flip(cur_arr,first_flip) 
            
            #now flip so next number is put into place
            cur_arr = self.flip(cur_arr,sorting_idx)
            
            #advance to next index to sort
            sorting_idx -= 1
            
        return self.flips
            