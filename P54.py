'''
54. Spiral Matrix
Medium

2227

557

Add to List

Share
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return matrix
        
        if len(matrix) == 1:
            return matrix[0]
    
        
        n, m = len(matrix), len(matrix[0])
        start_i, end_i = 0, len(matrix)-1
        start_j, end_j = 0, len(matrix[0])-1
        i, j = 0, 0
        
        ans = []
        
        while len(ans) < n*m:
            
            if i == start_i and start_j <= end_j:
                while j <= end_j:
                    ans.append(matrix[i][j])
                    j += 1
                j -= 1
                start_i += 1
                i += 1
            
            if j == end_j and start_i <= end_i:
                while i <= end_i:
                    ans.append(matrix[i][j])
                    i += 1
                i -= 1
                end_j -= 1
                j -= 1
                
            if i == end_i and start_j <= end_j:
                while j >= start_j:
                    ans.append(matrix[i][j])
                    j -= 1
                j += 1
                end_i -= 1
                i -= 1
                
            if j == start_j and start_i <= end_i:
                while i >= start_i:
                    ans.append(matrix[i][j])
                    i -= 1  
                i+= 1
                start_j += 1
                j += 1
                
                
        return ans 
            
        