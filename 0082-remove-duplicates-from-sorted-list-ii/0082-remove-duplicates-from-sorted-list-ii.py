# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        removed = None
        
        
        if not head:
            return head
        
        while head.next:
            if head.val == head.next.val:
                removed = head.val
                prev.next = head.next.next
                head = prev.next
                
                if not head:
                    return dummy.next
            
            else:
                if head.val == removed:
                    prev.next = head.next
                    head = prev.next
                else:
                    prev = prev.next
                    head = head.next
                    
        if head.val == removed:
            prev.next = head.next
            head = prev.next
                
        return dummy.next
    
    
    
    
    
            