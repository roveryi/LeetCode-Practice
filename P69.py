'''
69. Sqrt(x)
Easy

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
Accepted
558,814
Submissions
1,653,370
'''

# Binary Search

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        left = 1
        right = int(x/2+1)
        
        while True:
            
            mid = int((left + right)/2)
            
            if mid ** 2 > x:
                right = mid - 1    
                
            elif (mid+1)**2 > x:
                return mid
            
            else:
                left = mid + 1
                