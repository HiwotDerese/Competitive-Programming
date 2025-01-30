'''
Given a binary tree, determine if it is height-balanced


'''
class BinaryTree():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def checkHeightBalance(root):
    if not root:
        return True
    
    def calculateHeight(node):
        if not node:
            return 0
        
        return 1 + (max(calculateHeight(node.left), calculateHeight(node.right)))


    return abs(calculateHeight(root.left) - calculateHeight(root.right)) <= 1
    






















