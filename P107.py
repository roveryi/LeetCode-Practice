'''
107. Binary Tree Level Order Traversal II
Easy

1502

213

Add to List

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Accepted
354,012
Submissions
664,057
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        
        ans, level = [], [root]
        
        while root and level:
            
            ans.append([node.val for node in level])
            
            leaves = [(node.left, node.right) for node in level]
            
            level = [n for leaf in leaves for n in leaf if n]
            
        return reversed(ans)
            