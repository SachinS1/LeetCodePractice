from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> int:
        
        #create a dictionary to store the graph
        graph = {i: [] for i in range(numCourses)}
        #course order
        courseOrder = []
        for prereq, course in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses

        def depth_first_search(course):
            if visited[course] == 1: #detected cycle
                return False
            if visited[course] == 2: #already visited
                return True
            
            visited[course] = 1

            for neighbor in graph[course]:
                if not depth_first_search(neighbor):
                    return False
            
            visited[course] = 2

            courseOrder.append(course)

            return True

        for i in range(numCourses):
            if depth_first_search(i) == False:
                return []
        

        return courseOrder[::-1]