#Charlie Miller
#Leetcode - 189. Rotate Array
#https://leetcode.com/problems/rotate-array/

"""
Place each element in righful place while putting
the overwritten value in a temp variable. Works well
when there's only 1 cycle. In cases where there's more
than 1 cycle, do it for each cycle. Each cycle is orthogonal
and offset by 1
Time: O(n) Space: O(1)

Sln 2: Split array in 2 where the new array would end. Switch the
order of the two halves

Sln 3: Pop the last value of the array and append it to the beginning
for as many rotations needed (mod with length of array to not redo work)
"""

class Solution:
    def get_factors(self,num):
        #1 and the number will always be factors
        factors = [1,num]
        
        #if it's a square number, only add it's sqrt once
        root = sqrt(num)
        if root.is_integer():
            factors.append(int(root))
            
        #all other factors are in range 2 to the sqrt
        for cand in range(2,int(root)):
            if num % cand == 0:
                #add both numbers that need to multiply
                factors.append(cand)
                factors.append(num//cand)
                
        return factors
    
    #highest common factor
    def hcf(self,a,b):
        higher = max(a,b)
        lower = min(a,b)
        
        #hcf can only be as high as the lower number
        #get all factors of the lower number and test
        #sort desc so we test higher numbers first
        candidates = self.get_factors(lower)
        candidates.sort(reverse=True)
        
        #if a factor divides evenly, we got our factor
        for candidate in candidates:
            if higher % candidate == 0:
                return candidate
            
        return 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #check to see if we need to rotate at all
        true_rotations = k % len(nums)
        if true_rotations == 0:
            return
        
        #there will only be as many chains as the highest common factor
        #of the size of the array and the rotations
        chains = self.hcf(len(nums),true_rotations)
        
        #chains are orthogonal, so we can offset by just 1
        for chain_offset in range(chains):
            cur_idx = chain_offset
            cur_num = nums[cur_idx]
            first = True
            while cur_idx != chain_offset or first:
                #get the idx to swap out with
                next_idx = (cur_idx + true_rotations) % len(nums)
                #record value at next, then swap out with current
                temp = nums[next_idx]
                nums[next_idx] = cur_num
                #recorded value will be filling in the next spot
                cur_num = temp
                cur_idx = next_idx
                first = False