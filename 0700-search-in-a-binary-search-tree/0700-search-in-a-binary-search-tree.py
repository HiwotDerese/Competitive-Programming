# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while root.val != val:
            
            if val > root.val:
                if not root.right:
                    return None
                
                root = root.right
            else:
                if not root.left:
                    return None
                
                root = root.left
                
            
                
        return root
            
            