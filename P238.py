'''
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 2: return [nums[1], nums[0]]
        if len(nums) == 3: return [nums[1]*nums[2], nums[0]*nums[2], nums[0]*nums[1]]
        mid = int(len(nums)/2)
        left, right = 1, 1
        
        for i in range(mid):
            left *= nums[i]
        for i in range(mid, len(nums)):
            right *= nums[i]

        ans = [right*x for x in self.productExceptSelf(nums[0:mid])] + [left*x for x in self.productExceptSelf(nums[mid:len(nums)])] 
        
        
        return ans 

# Solution from discussion
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output