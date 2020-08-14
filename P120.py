'''
120. Triangle
Medium

2035

243

Add to List

Share
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) == 0:
            return 0
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        dp = triangle
        
        for i in range(1, len(triangle)):
            dp[i][0] += dp[i-1][0] 
            dp[i][-1] += dp[i-1][-1]
            
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        
        return min(dp[-1]) 
            