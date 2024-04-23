# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        dic = defaultdict(int)
        dic[0] = 1
        self.sum = 0

        def backtrack(node):
            # print(dic)
            if not node:
                return
            # print(node.val, self.sum)
            self.sum += node.val
            # print(node.val, self.sum)

            if self.sum - targetSum  in dic:
                # print(self.ans, self.sum, "anssss")
                self.ans += dic[self.sum - targetSum]

            dic[self.sum] += 1
    
            left = backtrack(node.left)
            right = backtrack(node.right)

            dic[self.sum] -= 1
            self.sum -= node.val

        backtrack(root)
        return self.ans