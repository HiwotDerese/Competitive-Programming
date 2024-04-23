# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        i = head
        j = head.next
        while j:
            if i.val <= j.val:
                i = i.next
                j = j.next
            else:
                temp = dummyNode
                while temp.next.val <= j.val:
                    temp = temp.next
                i.next = j.next
                j.next = temp.next
                temp.next = j
                j = i.next
        return dummyNode.next