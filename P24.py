'''
24. Swap Nodes in Pairs
Medium

1547

137

Favorite

Share
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        temp1, temp2 = head, head.next 
        temp1.next = temp2.next 
        temp2.next = temp1
        temp2.next.next = self.swapPairs(temp2.next.next)
        
        return temp2
        