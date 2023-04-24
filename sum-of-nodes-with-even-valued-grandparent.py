# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, parent, grandparent):
        if not root:
            return

        if grandparent % 2 == 0:
            self.ans += root.val


        self.dfs(root.left, root.val, parent)
        self.dfs(root.right, root.val, parent)


    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        self.dfs(root, 1, 1)

        return self.ans