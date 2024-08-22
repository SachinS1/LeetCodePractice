from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #function to calculate the depth of a  binary tree
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if root is None:
            return -1
        #recursion
        ldepth = self.calculateDepth(root.left)
        rdepth = self.calculateDepth(root.right)

        #for last element (leaf), the depth is 0 [-1 + 1]
        return max(ldepth, rdepth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        ldepth = self.calculateDepth(root.left)
        rdepth = self.calculateDepth(root.right)

        if abs(ldepth - rdepth) > 1:
            return False
        

        return self.isBalanced(root.left) and self.isBalanced(root.right)