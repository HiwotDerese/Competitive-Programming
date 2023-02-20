# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Hset = set()
        
        while head:
            if head in Hset:
                return head
            Hset.add(head)
            head = head.next 
            
        return 
        