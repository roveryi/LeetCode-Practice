'''
46. Permutations
Medium

3792

104

Add to List

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.dfs(nums, [], res)
        
        return res
        
    
    def dfs(self, nums, path, res):
        
        if not nums:
            res.append(path)
            
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)