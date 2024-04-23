# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            ans.append(root.val)
            
            inorder(root.right)
            
        
         
            
        ans = []
        inorder(root)
        return ans
        
#         if not root.left:
#             return root.val
        
#         return inorderTraversal(root.left)
    
        
        
            
        
        
        