'''
124. Binary Tree Maximum Path Sum
Hard

3798

296

Add to List

Share
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
Accepted
378,045
Submissions
1,105,015
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def sums(root):
            if not root:
                return [-float('inf'), -float('inf')]
            
            left = sums(root.left)
            right = sums(root.right)
            
            return [root.val + max(left[0], right[0], 0),
                   max(left + right + [root.val + left[0] + right[0]])] 
            
        return max(sums(root))
        