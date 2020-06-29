'''
55. Jump Game
Medium

4102

321

Add to List

Share
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        if nums[0] == 0: 
            return False
        
        dp = [i != 0 for i in nums]
        idx = [i for i, v in enumerate(nums) if v == 0]
        
        if nums[-1] == 0:
            dp[-1] = True
            idx.pop()
        idx.insert(0, 0)
                
        for i in reversed(range(1, len(idx))):
            for j in reversed(range(idx[i-1], idx[i])):
                
                states = [dp[k] for k in range(j+1, min(j+nums[j]+1, len(nums)))]

                if states == [False] * len(states):
                    dp[j] = False
                    
                else: dp[j] = True

        return dp[0]  


# nicer 
class Solution:
    def canJump(self, nums: List[int]) -> bool:          
    
        i, lastPos = len(nums) - 1, len(nums) - 1
        
        while i >= 0:
            
            if i + nums[i] >= lastPos:
                lastPos = i
            
            i -= 1
        
        return lastPos == 0
        
                    
