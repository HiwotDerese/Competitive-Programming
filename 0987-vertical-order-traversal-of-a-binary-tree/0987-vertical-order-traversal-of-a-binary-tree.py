# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def vertical(root, col, row):
            if not root:
                return
            
            
            
            if (col, row) in dic:
                dic[(col, row)].append(root.val)
            else:
                dic[(col, row)] = [root.val]
                
            leftVertical = vertical(root.left, col - 1, row + 1)
            
            
                
            rightVertical = vertical(root.right, col + 1, row + 1)
            
            
        
        
        
        
        dic = {}
        col = 0
        
        vertical(root, 0, 0)
        ans = []
        
        sortedDic = sorted(dic)
        # print(sortedDic)
        
        for i in sortedDic:
            # print(i, dic[i], i[0], i[1])
            if len(dic[i]) > 1:
                dic[i].sort()
            ans.append(dic[i])
        # print(ans)
            
        dic2, j = {}, 0
        for i in sortedDic:
            if i[0] in dic2:
                dic2[i[0]] += ans[j]
            else:
                dic2[i[0]] = ans[j]
                # print(dic2)
                
            j += 1
                
        # print(dic2)
        ans2 = []
        for i in dic2:
            ans2.append(dic2[i])

            
        return ans2
        
        
        # print(dic)
        