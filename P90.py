'''
90. Subsets II
Medium

1732

75

Add to List

Share
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Accepted
286,426
Submissions
607,993
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        ans = []
        
        def DFS(can, path):
            if path not in ans:
                ans.append(path)
            for i in range(len(can)):
                DFS(can[i+1:], sorted(path + [can[i]]))
                
        DFS(nums, [])
        
        return ans