# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         length = 0
#         while curr:
#             length += 1
#             curr = curr.next
            
#         mid = length // 2
        
#         while mid:
#             head = head.next
#             mid -= 1
            
#         return head
    
    
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
            
        return arr[len(arr) // 2]
         
            
    
    
        
            
        
        
        
        # tail = head
        # while head and head.next:
        #     tail = tail.next
        #     head = head.next.next
        # return tail
        