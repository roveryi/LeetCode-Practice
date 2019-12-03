'''
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution:
	def combinationSum(self, candidates, target):
		candidates.sort()
		ans = []

		def dfs(target, idx, path):
			if target < 0:
				return 

			if target == 0:
				ans.append(path)
				return 

			for i in range(idx, len(candidates)):
				dfs(target - candidates[i], i, path + candidates[i])

		dfs(target, 0, [])

		return ans


'''
My trail
''' 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if len(candidates) == 0 or target < min(candidates): 
            return 
        if len(candidates) == 1 and target%candidates[0] == 0: 
            return [candidates[0]]*int(target/candidates[0])
        
        ans = []

        for i in range(int(target/candidates[0])+1):
            cur = [candidates[0]]*i
            if target - i*candidates[0] == 0:
                ans.append(cur)
                
            if self.combinationSum(candidates[1:], target - i*candidates[0]):
                ans.append(cur + self.combinationSum(candidates[1:], target - i*candidates[0]))
                
        return ans
            