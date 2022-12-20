# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        ans = []
        i = 0
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                ans[stack.pop()[0]] = head.val
            stack.append((i, head.val))
            head = head.next
            i += 1
        
        return ans

        