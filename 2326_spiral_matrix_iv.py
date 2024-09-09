from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        #fill everything with -1
        final_matrix = [[-1]*n for _ in range(m)]
        #direction vectors
        direction_vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0
        curr_pos_x, curr_pos_y = 0, 0
        while head:
            final_matrix[curr_pos_x][curr_pos_y] = head.val
            head = head.next

            next_x = curr_pos_x + direction_vector[direction_idx][0]
            next_y = curr_pos_y + direction_vector[direction_idx][1]
            #check if it falls in range and if its already filled
            if (0 <= next_x < m and 0 <= next_y < n and final_matrix[next_x][next_y] == -1):
                curr_pos_x, curr_pos_y = next_x, next_y
            else:
                #flip direction if already filled
                direction_idx = (direction_idx + 1) % 4
                curr_pos_x = curr_pos_x + direction_vector[direction_idx][0]
                curr_pos_y = curr_pos_y + direction_vector[direction_idx][1]
        return final_matrix