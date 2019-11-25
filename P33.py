'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        # Edge cases
        if len(nums) == 0: return -1
        if len(nums) == 1: 
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            return -1 if target not in nums else nums.index(target)

        left, mid, right = 0, int(len(nums)/2), len(nums)-1
        while left < right-1:
            if target == nums[left]: return left
            if target == nums[mid]: return mid
            if target == nums[right]: return right 
            
            # Inversion point after mid point
            if nums[left] < nums[mid]:
                # Target in the right 
                if (target < nums[left] and target < nums[mid]) or (target > nums[left] and target > nums[mid]):
                    left = mid
                    mid = int((left + right)/2)

                # Target in the left
                elif  (target > nums[left] and target < nums[mid]) :
                    right = mid
                    mid = int((left + right)/2)
                
                # Not possible
                elif (target < nums[left] and target > nums[mid]): 
                    return -1
                
            # Inversion point before mid point
            elif nums[left] > nums[mid]:
                # Target in the left 
                if (target < nums[left] and target < nums[mid]) or (target > nums[left] and target > nums[mid]):
                    right = mid
                    mid = int((left + right)/2)
                    
                # Target in the right
                elif (target < nums[left] and target > nums[mid]):
                    left = mid
                    mid = int((left + right)/2)
                
                # Not possible
                elif (target > nums[left] and target < nums[mid]): 
                    return -1
            
        return -1
        