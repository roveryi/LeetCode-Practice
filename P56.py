'''
56. Merge Intervals
Medium

4161

284

Add to List

Share
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Leetcode answer

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        
        intervals.sort(key = lambda x: x[0])
        
        for interval in intervals:
            
            # the upper bound of prior interval is smaller than the lower bound of current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                
                
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged