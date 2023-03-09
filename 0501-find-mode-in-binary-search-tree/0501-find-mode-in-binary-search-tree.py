# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def mode(root, dic):
            
            if not root:
                return
            
            if root.val in dic:
                dic[root.val] += 1
                
            else:
                dic[root.val] = 1
                
            mode(root.left, dic)
            mode(root.right, dic)
               
    
        dic = {}
        mode(root, dic)
        
        sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        most_freq = sorted_dic[0][1]
        
        ans, i = [], 0
        while i < len(sorted_dic) and sorted_dic[i][1] == most_freq:
            ans.append(sorted_dic[i][0])
            i += 1
            
        return ans
        