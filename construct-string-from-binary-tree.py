# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root):
        if not root:
            return 

        self.ans += str(root.val)

        if not root.left and not root.right:
            return

        self.ans += "("
        self.preOrder(root.left)
        self.ans += ")"
        
        if root.right:
            self.ans += "("
            self.preOrder(root.right)
            self.ans += ")"


    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        self.preOrder(root)
        return self.ans