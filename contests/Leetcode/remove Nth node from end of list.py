# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head2 = dummy = ListNode(0, head)
        tail = head
        for i in range(n):
            tail = tail.next
        while tail:
            head2 = head2.next
            tail = tail.next
        head2.next = head2.next.next
        return dummy.next
        
        