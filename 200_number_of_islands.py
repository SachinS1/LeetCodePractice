from typing import List

class Solution:

    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def depth_first_search(self, i, j, grid):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'        
        for di, dj in self.directions:
            self.depth_first_search(i+di, j+dj, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        x = len(grid)
        y = len(grid[0])

        for i in range(0, x):
            for j in range(0, y):
                if grid[i][j] == '1':
                    islands += 1
                    self.depth_first_search(i, j, grid)
        
        return islands