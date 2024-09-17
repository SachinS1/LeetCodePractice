from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if not intervals:
            return []

        output = []
        first = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= first[1]:
                first = [first[0], max(intervals[i][1], first[1])]
            else:
                output.append(first)
                first = intervals[i]
        output.append(first)
        return output
        