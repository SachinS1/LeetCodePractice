from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)} #create a dictionary to store a graph

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses #visited list to keep track of nodes

        def depth_first_search(course):
            if visited[course] == 1:
                return False
            elif visited[course] == 2:
                return True
        
            visited[course] = 1

            for neighbour in graph[course]:
                if not depth_first_search(neighbour):
                    return False
            
            visited[course] = 2
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not depth_first_search(course):
                    return False
        
        return True
