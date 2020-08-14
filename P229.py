'''
229. Majority Element II
Medium

1572

167

Add to List

Share
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
Accepted
143,476
Submissions
405,062
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        
        left, right = 0, int(len(nums)//3)
        
        ans = []
        
        while right < len(nums):
            
            if (nums[left] == nums[right]) and (nums[left] not in ans):
                ans.append(nums[left])
                
            left += 1
            right += 1
                
            
        return ans