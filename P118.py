'''
118. Pascal's Triangle
Easy

1505

110

Add to List

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
385,314
Submissions
737,732
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def nextRow(cur):
            return [1] + [cur[i] + cur[i+1] for i in range(len(cur)-1)] + [1]
        
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        dp = [None for i in range(numRows)]
        dp[0] = [1]
        dp[1] = [1,1]
        
        for i in range(2, numRows):
            dp[i] = nextRow(dp[i-1])
            
        return [i for i in dp]