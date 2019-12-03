'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def dfs(target, idx, path):
            
            if target < 0: 
                return 
            if target == 0: 
                ans.append(path)
                return 
            for i in range(idx, len(candidates)):
                dfs(target - candidates[i], i+1, path+[candidates[i]])
        
        dfs(target, 0, [])
        
        unique = []
        
        for i in ans:
            if i not in unique: unique.append(i)
        
        return unique