'''
25. Reverse Nodes in k-Group
Hard

2062

356

Add to List

Share
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1:
            return head
        
        t = head 
        ans = ListNode(0)
        temp = ans
        
        while t:
            r, m = self.reverse(t, k)
            while temp.next:
                temp = temp.next 
            temp.next = r
            t = m
            
        return ans.next
            
        
    def reverse(self, l, k):
        #reverse the entire list 
        r = ListNode(l.val)
        temp = l.next
        count = 1
        
        while count < k:
            if temp:
                r = ListNode(temp.val, r)
                
                if temp.next:
                    temp = temp.next
                    count += 1
                else:
                    break
            else: 
                break
                    
        if count < k-1:
            return l, None
        elif count == k-1:
            return r, None
        else:
            return r, temp
    