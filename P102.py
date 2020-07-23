'''
102. Binary Tree Level Order Traversal
Medium

3081

76

Add to List

Share
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Accepted
623,177
Submissions
1,147,392
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        ans, level = [], [root]
        
        while root and level:
            ans.append([node.val for node in level])
            leaves = [(node.left, node.right) for node in level]
            level = [l for leaf in leaves for l in leaf if l]
            

        return ans