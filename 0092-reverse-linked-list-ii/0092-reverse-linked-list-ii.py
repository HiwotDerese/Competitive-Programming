# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        for i in range(left - 1):
            prev = curr
            curr = curr.next
            
        num1 = prev
        num2 = curr
        prev2 = None
        
        for i in range(right - left):
            temp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = temp
            
        num1.next = curr
        num2.next = curr.next
        if prev2:
            curr.next = prev2
        
        return dummy.next