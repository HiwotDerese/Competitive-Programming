# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lower, upper):
            
            if not root:
                return True
            
            if (root.val <= lower) or (root.val >= upper):
                return False
            
            validLeft = isValid(root.left, lower, root.val)
            validRight = isValid(root.right, root.val, upper)
            
            return validLeft and validRight
            
            
            
        
        return isValid(root, -float('inf'), float('inf'))
#         def inorder(root):
#             if not root:
#                 return
            
#             inorder(root.left)
#             if root:
#                 ans.append(root.val)
#             inorder(root.right)
        
#         ans = []
#         inorder(root)
        
#         if len(ans) == 1:
#             return True
        
#         i, leng = 1, len(ans)
#         while i < leng:
            
#             if (i + 1) < leng:
#                 if ans[i - 1] < ans[i] and ans[i + 1] > ans[i]:
#                     i += 2
                    
#                 else:
#                     return False
                    

#             elif ans[i - 1] < ans[i]:
#                 i += 2
                
#             else:
#                 return False
                
            
#         return True
    
    

    
    
    
    
    
    