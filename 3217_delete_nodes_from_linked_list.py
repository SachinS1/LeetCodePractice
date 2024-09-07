# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # change to set for faster search
        nums = set(nums)

        #this is done so that it points to the beginning of the list via dummy.next (always)
        dummy = ListNode()
        dummy.next = head

        #two pointers: previous node and current node
        prev = dummy
        curr = head

        while curr:
            if curr.val not in nums:
                prev = prev.next
                curr = curr.next
            else:
                #to delete: we just move the pointer for prev.next (we skip over curr)
                prev.next = curr.next
                curr = curr.next
        
        return dummy.next