# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greate_eq = ListNode()

        last1, last2 = less, greate_eq

        while head:
            if head.val < x:
                last1.next = head
                last1 = last1.next

            else:
                last2.next = head
                last2 = last2.next

            head = head.next

        # print(less)
        # print(greate_eq)
        last1.next = greate_eq.next
        last2.next = None
         
        return less.next