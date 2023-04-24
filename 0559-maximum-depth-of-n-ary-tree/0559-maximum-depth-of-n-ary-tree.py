"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def depth(self, root, count, ans):
        # print(ans)
        if not root.children:
            ans.append(count + 1)

            return

        for i in root.children:
            self.depth(i, count + 1, ans)
    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = []
        self.depth(root, 0, ans)
        return max(ans)
        
        
        
        
        
    
    
        