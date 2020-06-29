'''
47. Permutations II
Medium

1879

60

Add to List

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        self.dfs(nums,[], res)
                
        return res
        
    def dfs(self, nums, path, res):

        if not nums and path not in res:
            res.append(path)

        for i in range(len(nums)):

            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)