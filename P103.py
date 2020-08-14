'''
103. Binary Tree Zigzag Level Order Traversal
Medium

2206

102

Add to List

Share
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Accepted
382,176
Submissions
796,841
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        ans, level = [], [root]
        l = 0
        
        while root and level:
            
            ans.append([node.val for node in level])
            
            if l %2 == 0:
                leaves = [(node.right, node.left) for node in reversed(level)]
            else:
                leaves = [(node.left, node.right) for node in reversed(level)]
                
            level = [n for leaf in leaves for n in leaf if n]
            l += 1
            
        return ans
                