# Charlie Miller
# Leetcode - 952. Largest Component Size by Common Factor
# https://leetcode.com/problems/largest-component-size-by-common-factor/


"""
This following is a snapshot of the answer I came up with, without help. 
More optimal solution found here:
https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/819919/Python-Union-find-solution-explained

My (sub-optimal) approach:
search for a common factor in every pair of numbers in the array
Perform a disjoint set union for every pair that does have a common factor
keep track of set sizes separately, adding root totals when a set is joined
Time complexity: O(n^2 * sqrt(m)), where n is array size, and m is the second largest number that appears
Space complexity: O(n)
"""

class Solution:
    def get_factors(self,num):
        #We only need to search up to the square root
        max_check = int(math.sqrt(num))
        
        #number itself is a factor
        factors = [num]
        
        #check every number if it's divisible, if so add both factors
        for candidate in range(2,max_check+1):
            if num % candidate == 0:
                other = num//candidate
                factors.append(candidate)
                factors.append(other)
                
        return factors
                
    def has_common_factor(self,a,b):
        #Find the factors of the smaller number, see if any of those
        #factors are shared with the larger
        
        if a < b:
            smaller = a
            larger = b
        elif b < a:
            smaller = b
            larger = a
        else:
            #they're the same, so they have the same factors
            return True
        
        #Exclude 1, as described by the problem
        if smaller == 1:
            return False

        #Optimization: short-circuit if they're both even
        if smaller % 2 == 0 and larger % 2 == 0:
            return True

        # Test if the smaller number shares factors with the larger
        smaller_factors = self.get_factors(smaller)
        for factor in smaller_factors:
            if larger % factor == 0:
                return True
            
            
        return False
    
    def get_root(self,idx):
        #DSU - get root by traveling down parent tree, until parent is itself
        cur_idx = idx
        while cur_idx != self.roots[cur_idx]:
            cur_idx = self.roots[cur_idx]

        #to flatten tree, assign number's root to the true root
        self.roots[idx] = cur_idx
        return cur_idx
    
    def largestComponentSize(self, A):
        #create array for Disjoint Set Union - roots are each node's parents
        size = len(A)
        self.roots = list(range(size))
        
        #Keep track of the sizes for each set here
        disjoint_set_sizes = [1 for _ in range(len(A))]
                     
        #determine if each pair has a common factor
        for i in range(size-1):
            num = A[i]
            for j in range(i+1,size):
                num_root = self.get_root(i)
                other_root = self.get_root(j)
                # print(i,j,self.roots,disjoint_set_sizes)
                
                #They belong to the same set already - we can move on
                if num_root == other_root:
                    continue
                    
                #If they don't have a common factor, move on
                other = A[j]
                if not self.has_common_factor(num,other):
                    continue
                    
                #join the sets
                self.roots[other_root] = num_root
                self.roots[j] = num_root
                
                #add the size of the two sets together
                disjoint_set_sizes[num_root] += disjoint_set_sizes[other_root]
                
        return max(disjoint_set_sizes)