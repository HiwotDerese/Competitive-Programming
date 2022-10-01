# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        head2 = head
        prev = dummyNode
        tail = head.next
        while head2:
            while tail and head2.val == tail.val:
                head2 = tail
                tail = tail.next
            if prev.next == head2:
                prev = prev.next
                head2 = tail
                # tail = tail.next
            else:
                prev.next = tail
                head2 = prev.next
                # tail = tail.next
        return dummyNode.next

