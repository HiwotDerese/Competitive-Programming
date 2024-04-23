# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def paths(self, root, arr):
        if not root:
            return

        if not root.left and not root.right:
            arr += [str(root.val)]
            num = "".join(arr)
            print(num, "num")
            self.ans += int(num)

            return
        
        self.paths(root.left, arr + [str(root.val)])

        self.paths(root.right, arr + [str(root.val)])

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.paths(root, [])

        return self.ans