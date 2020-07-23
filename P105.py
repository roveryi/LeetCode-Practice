'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

3447

93

Add to List

Share
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
Accepted
364,093
Submissions
752,270
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None    
        
        Tree = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        
        left, num_left = inorder[:idx], len(inorder[:idx])
        right, num_right = inorder[idx+1:], len(inorder[idx+1:])
        
        Tree.left = self.buildTree(preorder[1:num_left+1], left)
        Tree.right = self.buildTree(preorder[num_left+1:], right)
                
        return Tree
