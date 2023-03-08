# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root, level):
            if not root:
                return
            
            
            level += 1
            levelOrder(root.left, level)
            if level in dic:
                dic[level].append(root.val)
            else:
                dic[level] = [root.val]
                
            levelOrder(root.right, level)
    
            
        dic = {}
        levelOrder(root, 0)
        sortedDic = sorted(dic)
        ans = []
        for i in sortedDic:
            ans.append(dic[i][-1])
            
        
        return ans
        