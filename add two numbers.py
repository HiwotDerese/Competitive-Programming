# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        LinkedList = head
        sums  = 0
        while l1 or l2 or sums:
            if l1:
                sums += l1.val
                l1 = l1.next
            if l2:
                sums += l2.val
                l2 = l2.next
            head.next = ListNode(sums % 10)
            head = head.next
            sums = sums // 10
        return LinkedList.next
            
            
        
        