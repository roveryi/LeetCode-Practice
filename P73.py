'''
73. Set Matrix Zeroes
Medium

2255

309

Add to List

Share
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Accepted
326,914
Submissions
758,399
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
    
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    
                    for p in range(m):
                        if matrix[i][p] != 0:
                            matrix[i][p] = 'a'
                            
                    for p in range(n):
                        if matrix[p][j] != 0:
                            matrix[p][j] = 'a'
                            

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
            
                    
        return None