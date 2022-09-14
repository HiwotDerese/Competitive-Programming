# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currHead = head
        while currHead and currHead.next:
            if currHead.val == currHead.next.val:
                currHead.next = currHead.next.next
            else:
                currHead = currHead.next
        if not currHead:
            return head
        return head
        