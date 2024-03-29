# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if root.val > val:
            # if not root.left:
            #     return None
        
            return self.searchBST(root.left, val)
        
        # if not root.right:
        #     return None
        
        return self.searchBST(root.right, val)
        
        
#         while root.val != val:
            
#             if val > root.val:
#                 if not root.right:
#                     return None
                
#                 root = root.right
#             else:
#                 if not root.left:
#                     return None
                
#                 root = root.left
                
           
#         return root
            
            