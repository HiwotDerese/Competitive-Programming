# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         Hset = set()
        
#         while head:
#             if head in Hset:
#                 return head
#             Hset.add(head)
#             head = head.next 
            
#         return 

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        if not fast or not fast.next:
            return
            
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
            
            
            
            
            
            
            
        