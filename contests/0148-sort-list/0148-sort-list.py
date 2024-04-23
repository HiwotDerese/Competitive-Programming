# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def divide(self, slow, fast):
        # slow, fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   
        return slow
    
    
    def conquer(self, first_half, second_half):
        ans = dummy = TreeNode()
        while first_half and second_half:
            if first_half.val <= second_half.val:
                ans.next = first_half
                first_half = first_half.next
            else:
                ans.next = second_half
                second_half = second_half.next
            ans = ans.next
            
        if first_half:
            ans.next = first_half
        if second_half:
            ans.next = second_half
                
        return dummy.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_half = head
        second_half = self.divide(head, head.next)
        temp = second_half.next
        second_half.next = None
        second_half = temp
        

        first_half = self.sortList(first_half)
        second_half = self.sortList(second_half)
        
        return self.conquer(first_half, second_half)
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not head: return None
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # arr.sort()
        # sortedA = ListNode()
        # ans = sortedA
        # for i in arr:
        #     sortedA.next = ListNode(i)
        #     sortedA = sortedA.next
        # return ans.next