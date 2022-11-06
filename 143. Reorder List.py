# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack=[]
        temp, temp2 = head, head
        while temp:
            stack.append(temp)
            temp = temp.next
        for i in range(len(stack)//2):
            top = stack.pop()
            nxt = temp2.next
            temp2.next = top
            top.next = nxt
            temp2 = nxt
        temp2.next=None    
        