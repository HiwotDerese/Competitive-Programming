'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

              3
        9          20
                15     7

                [[3], [9, 20], [15, 7]]
'''
from collections import deque

class BinaryTree():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return []
    
    queue = deque()
    visited = set()
    queue.append(root)
    visited.add(root)
    ans = []

    while queue:
        level = []
        len_ = len(queue)

        # iterate through elements in one level
        for i in range(len_):
            curr = queue.popleft()
            level.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        ans.append(level)

    return ans



# root = [3,9,20,null,null,15,7]

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20, BinaryTree(15), BinaryTree(7))

print(bfs(root))
#  [[3],[9,20],[15,7]]


        




