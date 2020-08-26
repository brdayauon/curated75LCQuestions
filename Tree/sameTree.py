# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
        
        #if p == None and q == None:  #if p is none and q is none return true
         #   return True
        #if q == None or p == None: #if q is none Or P is none return False
         #   return False
        
       # if p.val != q.val:  #if val of p is not equal to val of q return False
        #    return False
        
        #return (call function recursively but the right and left side)
        #return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)