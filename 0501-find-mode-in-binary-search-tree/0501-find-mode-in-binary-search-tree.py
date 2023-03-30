# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, dic):
            
            if not root:
                return
            
            self.inorder(root.left, dic)
            
            dic[root.val] = dic.get(root.val, 0) + 1
                
            self.inorder(root.right, dic)
            
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:     
        dic = {}
        
        self.inorder(root, dic)
        
        sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        most_freq = sorted_dic[0][1]
        
        ans, i = [], 0
        
        while i < len(sorted_dic) and sorted_dic[i][1] == most_freq:
            ans.append(sorted_dic[i][0])
            i += 1
            
        return ans
        