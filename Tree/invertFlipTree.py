# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        rightTree = self.invertTree(root.right)
        leftTree = self.invertTree(root.left)
        
        root.right = leftTree
        root.left = rightTree
        
        return root