# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        first = 0
        last = len(arr) - 1
        while first < last:
            if arr[first] != arr[last]:
                return False
            first += 1
            last -= 1
        return True
                
        