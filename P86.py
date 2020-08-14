'''
86. Partition List
Medium

1365

304

Add to List

Share
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
Accepted
219,980
Submissions
530,386
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if not head:
            return None
        
        vals = []
        pointer = head
                
        while pointer:
            vals.append(pointer.val)
            pointer = pointer.next 
        i = 0
        reorder = []
        while i < len(vals):
            if vals[i] >= x:
                i += 1
            else:
                reorder.append(vals[i])
                vals.pop(i)       
        vals = reorder + vals 
        ans = ListNode(vals[0])
        t = ans
        for i in range(1, len(vals)):
            t.next = ListNode(vals[i])
            t = t.next
        return ans


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        
        temp = ListNode(-float('inf'), head)
        p = temp
        
        l = ListNode(val = 0, next = None)
        t = l
        
        while p.next:
            if p.next.val < x:
                p = p.next
                
            else:
                t.next = ListNode(p.next.val)
                t = t.next
                p.next = p.next.next
        
        p.next = l.next
        
        return temp.next