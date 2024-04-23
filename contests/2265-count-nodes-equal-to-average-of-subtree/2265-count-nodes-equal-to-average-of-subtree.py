# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sums(self, root, asn):
            
        if not root:
            return [0, 0]


        leftSum = self.sums(root.left, self.ans)
        # self.node += 1

        rightSum = self.sums(root.right, self.ans)

        ave =  (leftSum[0] + rightSum[0] + root.val) // (leftSum[1] + rightSum[1] + 1)
        # print(leftSum, rightSum, (leftSum[1] + rightSum[1] + 1), (leftSum[0] + rightSum[0] + root.val))
        # print(ave, root.val)

        if ave == root.val:
            # print(ave, root.val, leftSum, rightSum)
            self.ans += 1

        return [leftSum[0] + rightSum[0] + root.val, leftSum[1] + rightSum[1] + 1]
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.sums(root, self.ans)
        return self.ans
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        