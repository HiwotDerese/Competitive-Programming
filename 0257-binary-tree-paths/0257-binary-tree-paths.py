# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def path(self, root, one_path, ans):
        # print(one_path, root)
        if not root.left and not root.right:
            # one_path += str(root.val)
            # ans.append(one_path)
            ans.append(one_path[::] + [str(root.val)])
            # print(ans, root.val)
            return ans
        
        else:
            candidates = []
            if root.left:
                candidates.append(root.left)
            if root.right:
                candidates.append(root.right)

            for i in (candidates):
                
                # print(root.val)
                # print(one_path)
                one_path += [str(root.val)]
                # print(one_path)
                self.path(i, one_path, ans)
                one_path.pop()
                # print(root.val)
                # print(one_path)
                # if root.val < 0:
                #     one_path = one_path[:len(one_path) - 4]
                # else:
                #     one_path = one_path[:len(one_path) - 3]

            return [ *map('->'.join, ans) ]
                

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return str(root.val)
        
        ans, one_path = [], []
        return self.path(root, one_path, ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
               