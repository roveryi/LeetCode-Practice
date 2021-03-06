'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0: return [-1,-1]
        start, end, mid = 0, n-1, int(n/2)
        
        while end >= start:
            if end == start and target == nums[start]: return [start, start]
            if [target]*(end-start+1) == nums[start:end+1]: return [start, end]
            
            if target > nums[mid]:
                start = mid+1
                mid = int((start+end)/2)
            elif target < nums[mid]:
                end = mid-1
                mid = int((start+end)/2)
            else:
                if target > nums[start]:
                    start += 1
                elif target == nums[start]:
                    if start -1 >= 0 and target == nums[start-1]:
                        start -= 1
                    
                if target < nums[end]:
                    end -= 1
                elif target == nums[end]:
                    if end +1 < n-1 and target == nums[end+1]:
                        end += 1
                
        return [-1,-1]

