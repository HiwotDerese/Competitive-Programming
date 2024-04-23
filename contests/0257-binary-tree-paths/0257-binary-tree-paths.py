# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def path(self, root, one_path, ans):
        if not root.left and not root.right:
            
            ans.append(one_path + [str(root.val)])

            return ans
        
        else:
            candidates = []
            if root.left:
                candidates.append(root.left)
            if root.right:
                candidates.append(root.right)

            for i in (candidates):
                one_path += [str(root.val)]

                self.path(i, one_path, ans)
                
                one_path.pop()
                
            return [ *map('->'.join, ans) ]
                

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return str(root.val)
        
        ans, one_path = [], []
        return self.path(root, one_path, ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
               