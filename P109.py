'''
109. Convert Sorted List to Binary Search Tree
Medium

2040

87

Add to List

Share
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
Accepted
245,704
Submissions
518,618
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        fast_ptr, slow_ptr = head.next.next, head 
        
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next 
            
        temp = slow_ptr.next 
        slow_ptr.next = None
        
        ans = TreeNode(temp.val)
        ans.left = self.sortedListToBST(head)
        ans.right = self.sortedListToBST(temp.next)
        
        return ans 