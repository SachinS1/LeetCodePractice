#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root:

            #check whether root.val in regards to p and q
            if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
                return root
            # if both are lower than root.val, go to the left
            elif p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            # if both are higher than root.val, go to the left
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q) 