from collections import defaultdict
from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_list = defaultdict(list)

        for i in range(len(edges)):
            a, b = edges[i] #nodes connected by edges
            prob = succProb[i]

            adj_list[a].append((b, prob))
            adj_list[b].append((a, prob))

        max_heap = [(-1, start_node)]
        best_prob = [0] * n
        best_prob[start_node] = 1

        while max_heap:
            current_prob, current_node = heapq.heappop(max_heap)
            current_prob = -current_prob #converting to positive (converted to negative previously to apply min_heap)

            if current_node == end_node:
                return current_prob

            for neighbour, edge_prob in adj_list[current_node]:
                new_prob = current_prob * edge_prob

                if new_prob > best_prob[neighbour]:
                    best_prob[neighbour] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbour))
        
        return 0