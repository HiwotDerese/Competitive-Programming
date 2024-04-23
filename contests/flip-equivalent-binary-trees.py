# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def equ(x, y):
            if not x and not y:
                return True

            if (not x and y) or (x and not y) or x.val != y.val:
                return False

            if (equ(x.left, y.right) and equ(x.right, y.left)) or (equ(x.left, y.left) and equ(x.right, y.right)):
                return True
                
            return False


        return equ(root1, root2)