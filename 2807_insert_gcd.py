from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head
        
        while current and current.next:
            
            gcd_value = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            
            new_node.next = current.next
            current.next = new_node

            current = new_node.next

        return head