from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #count the size of the linked list
    def countSize(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        
        return count
        
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = self.countSize(head)

        final_list = []
        #for figuring out the number of elements per list
        number_of_elems_per_list = count // k
        remainder = count % k 

        tracker = head

        for _ in range(k):
            current = tracker
            for _ in range(number_of_elems_per_list + (1 if remainder > 0 else 0) - 1):
                if tracker:
                    tracker = tracker.next
            
            if tracker:
                next_node = tracker.next
                tracker.next = None
                tracker = next_node
            
            else:
                next_node = None

            final_list.append(current)

            remainder -= 1
        

        return final_list
