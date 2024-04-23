# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            root = TreeNode(val)
            return root
        
        head = root
        
        def insert(root, parent):
            
            if not root:
                if val < parent.val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                    
                return 
                
            if root.val > val:
                insert(root.left, root)
            
            else:
                insert(root.right, root)
        
        
        
        insert(root, None)
        
        return head
        
        
        
        