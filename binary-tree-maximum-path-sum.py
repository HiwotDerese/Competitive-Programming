# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxm(self, root):
        if not root:
            return 0

        left = self.maxm(root.left)
        right = self.maxm(root.right)
        
        if left <= 0:
            path1 = 0
        else:
            path1 = left

        if right <= 0:
            path2 = 0
        else:
            path2 = right

        path3 = root.val + path1 + path2

        self.max_ = max(self.max_, path3)

        return max(root.val + path1, root.val + path2)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_ = -float('inf')

        return max(self.maxm(root), self.max_)