from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        
        elements = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Right, Down, Left, Up
        dir_idx = 0  # Start by moving right
        curr_x, curr_y = 0, 0  # Start at the top-left corner
        visited = set()

        for i in range(rows * cols):
            elements.append(matrix[curr_x][curr_y])
            visited.add((curr_x, curr_y))
            next_dir_x, next_dir_y = directions[dir_idx][0] + curr_x,\
            directions[dir_idx][1] + curr_y
            if (0 <= next_dir_x < len(matrix)) and (0 <= next_dir_y < len(matrix[0])) and (next_dir_x, next_dir_y)not in visited:
                curr_x, curr_y = next_dir_x, next_dir_y
            else:
                dir_idx = (dir_idx + 1) % 4
                curr_x, curr_y = curr_x + directions[dir_idx][0], curr_y + directions[dir_idx][1] 

        return elements