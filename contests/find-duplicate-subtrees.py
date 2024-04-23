# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        subtrees = defaultdict(int)

        def dfs(node):
            if not node:
                return "@"

            left = dfs(node.left)
            right = dfs(node.right)

            # print(node.val, left, right)
            curr = str(node.val) + " " + left + right

            subtrees[curr] += 1

            print(curr)
            if subtrees[curr] == 2:
                ans.append(node)

            return curr

        dfs(root)
        return ans