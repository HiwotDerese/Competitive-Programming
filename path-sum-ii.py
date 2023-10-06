# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
            
        ans = []

        def find_path(way, root):
            print(way, root.val)
            if not root.left and not root.right:
                if sum(way) == targetSum:
                    ans.append(way)

                return

            if root.left:
                find_path(way + [root.left.val], root.left)

            if root.right:
                find_path(way + [root.right.val], root.right)



        find_path([root.val], root)
        return ans