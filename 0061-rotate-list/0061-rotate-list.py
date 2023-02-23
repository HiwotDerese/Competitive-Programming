# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        
#         length of linked list
        length = 0
        while head:
            length += 1
            head = head.next
            
        k = k % length
        for i in range(k):
            head = dummy.next
            prev = dummy
            
            while head.next:
                prev = prev.next
                head = head.next
            
            
            head.next = dummy.next
            dummy.next = head
            prev.next = None

            
        return dummy.next
                
            
                
        