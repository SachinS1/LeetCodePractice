from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        #using breadth first search
        queue = [root]
        count = 1
        while queue:

            for _ in range(len(queue)):
                node = queue.pop(0)

                if not node.left and not node.right:
                    return count
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
        return count
        
        #using depth first search (recursion technique)

        # if not root.left and not root.right:
        #     return 1

        # left_depth = float('inf') if not root.left else self.minDepth(root.left)
        # right_depth = float('inf') if not root.right else self.minDepth(root.right)
        
        # return 1 + min(left_depth, right_depth)