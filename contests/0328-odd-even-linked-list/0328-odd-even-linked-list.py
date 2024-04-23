# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        if not head or not head.next:
            return head
        
        
        even = evenStart =  head.next
        
        while even.next:
            head.next = head.next.next
            even.next = even.next.next
            
            head = head.next
            if even.next:
                even = even.next
        

        head.next = evenStart
        
        
        return dummy.next
        
        
            
        
        