# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, left_):
            if not root:
                return 

            if root.left == None and root.right == None and left_ == True:
                ans[0] += root.val
            
            dfs(root.left, True)
            dfs(root.right, False)
        
        ans = [0]
        dfs(root,0)
        
        return ans[0]
        