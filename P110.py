'''
110. Balanced Binary Tree
Easy

2306

171

Add to List

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Accepted
453,802
Submissions
1,044,822
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def TreeHeight(root):
            if not root:
                return 0
            return max(TreeHeight(root.left), TreeHeight(root.right)) + 1 
        
        
        if not root:
            return 1
        
        dif = TreeHeight(root.left) - TreeHeight(root.right)
        
        if abs(dif) > 1:
            return False
        
        return (self.isBalanced(root.left)) & (self.isBalanced(root.right))