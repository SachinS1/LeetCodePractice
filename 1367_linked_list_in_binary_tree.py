# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
            
        if not head:
            return True

        def checkPath(head: ListNode, root:TreeNode) -> bool:
            
            if not head:
                return True

            if not root:
                return False

            if root.val == head.val:
            #if first element matches, check for downward path
                return (checkPath(head.next, root.left) or checkPath(head.next, root.right))
            return False

        return (checkPath(head, root) or self.isSubPath(head, root.left) or \
         self.isSubPath(head, root.right))
        
    
