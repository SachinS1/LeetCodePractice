from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            #recursive implementation to get all the roots
            root.left, root.right = self.invertTree(root.left), self.invertTree(root.right)

            #swap the left and right pointers
            root.left, root.right = root.right, root.left
            
        return root