# ```
# 138. Copy List with Random Pointer
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
# ```

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        
        dic = {}
        temp = head
        
        while temp:
            dic[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        
        while temp:
            if temp.next:
                dic[temp].next = dic[temp.next]
            if temp.random:
                dic[temp].random = dic[temp.random]
            temp = temp.next
                
        return dic[head]