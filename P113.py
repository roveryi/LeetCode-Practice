'''
113. Path Sum II
Medium

1797

66

Add to List

Share
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
Accepted
333,871
Submissions
719,459
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        ans = []
        
        def DFS(root, path, sum):
            if not root:
                return None
            
            if not root.left and not root.right and root.val == sum:
                path = path + [root.val]
                ans.append(path)
                
            sum -= root.val
            path = path + [root.val]
            
            DFS(root.left, path, sum)
            DFS(root.right, path, sum)
            
        DFS(root, [], sum)
        
        return ans