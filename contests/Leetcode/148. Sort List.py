# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        sortedA = ListNode()
        ans = sortedA
        for i in arr:
            sortedA.next = ListNode(i)
            sortedA = sortedA.next
        return ans.next