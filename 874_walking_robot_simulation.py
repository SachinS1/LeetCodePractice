from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #robot original position
        robot_location = [0, 0]
        #robot movements in clockwise order: north, east, south, west
        heading = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        heading_idx = 0

        euclidean_dist = 0
        #this is done to convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        for moves in commands:
            if moves == -2:
                heading_idx = (heading_idx - 1) % 4 # % 4 to wrap anything less than 0 as 0
            
            elif moves == -1:
                heading_idx = (heading_idx + 1) % 4 # % 4 to wrap anything greater than 3 as 3

            else:
            #breaking the total move into different individual moves
                for _ in range(0, moves):
                    next_x = robot_location[0] + heading[heading_idx][0]
                    next_y = robot_location[1] + heading[heading_idx][1]

                    if (next_x, next_y) in obstacle_set:
                        break
                    else:
                        robot_location = [next_x, next_y]
    
            current_dist = robot_location[0]**2 + robot_location[1]**2

            euclidean_dist = max(current_dist, euclidean_dist)
            
        return euclidean_dist