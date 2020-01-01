# 200. Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def MarkExplored(i,j):
            if grid[i][j] == "1":
                grid[i][j] = '0'
            
                if i > 0:
                    MarkExplored(i-1,j) 
                if i < len(grid)-1:
                    MarkExplored(i+1,j)
                if j > 0:
                    MarkExplored(i, j-1)
                if j < len(grid[i])-1:
                    MarkExplored(i, j+1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    MarkExplored(i,j)
                    ans += 1
        return ans 
                    