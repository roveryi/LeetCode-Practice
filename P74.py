'''
74. Search a 2D Matrix
Medium

1884

162

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False 
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        
        while i < m:
            
            if target > matrix[i][-1]:
                i += 1
                
            else:
                for j in range(n):
                    if matrix[i][j] == target:
                        return True
                    
                return False
                