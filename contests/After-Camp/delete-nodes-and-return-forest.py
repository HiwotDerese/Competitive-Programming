# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def dfs(root):
            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)
            if root.val in to_delete:
                if left:
                    ans.append(left)

                if right:
                    ans.append(right)
                return None

            else:
                curr = TreeNode(root.val)
                curr.left = left
                curr.right = right

                if root.val == start:
                    ans.append(curr)

                return curr

        start = root.val
        ans = []
        dfs(root)
        
        return ans



        
        