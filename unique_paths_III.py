# Charlie Miller
# Leetcode - 980. Unique Paths III
# https://leetcode.com/problems/unique-paths-iii/

"""
Do a dfs for the paths, keeping track of the 0 squares to go along
the way to make sure every square is stepped on before ending
For each square, mark it as an obstacle, sum up the paths for each direction,
then unmark as obstacle
"""

class Solution:
    def unique_paths(self,grid,x,y,remaining):
        #save what this square was
        this_square = grid[y][x]
        
        #mark this square as an obstacle
        grid[y][x] = -1
        
        
        #sum up possible paths if neigbors were taken
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        paths = 0
        for nx,ny in neighbors:
            #do not go out of bounds
            if not self.valid(nx,ny):
                continue
                
            #do not go into an obstacle
            if grid[ny][nx] == -1:
                continue
                
            #when end encountered, add 1 to paths only if we've traversed everything else first
            elif grid[ny][nx] == 2:
                paths += 1 if remaining == 0 else 0
                
            #sum from other paths, we took a step so 1 less square to traverse
            elif grid[ny][nx] == 0:
                paths += self.unique_paths(grid,nx,ny,remaining-1)
                
        #restore the value of this square so other paths may traverse it
        grid[y][x] = this_square
        
        return paths
            
    def valid(self,x,y):
        if x < 0 or y < 0:
            return False
        if x > self.width-1 or y > self.height-1:
            return False
        
        return True
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        self.width = len(grid[0])
        self.height = len(grid)
        
        
        #first iterate thru grid to determine how many steps we
        #have to take to consider the whole grid traversed, also
        #the location of the starting square so we know where to 
        #start our dfs
        self.zeros = 0 #how many steps we have to take
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == 0:
                    self.zeros += 1
                elif grid[y][x] == 1:
                    self.start = (x,y)
                elif grid[y][x] == 2:
                    self.end = (x,y)
                    
        paths = self.unique_paths(grid,self.start[0],self.start[1],self.zeros)
        return paths
        