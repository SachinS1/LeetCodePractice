from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        results = []

        for i in range(0, len(intervals)):
            #if the interval is to be appended before
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                return results + intervals[i:]
            #if the interval is to be appended after
            elif newInterval[0] > intervals[i][1]:
                results.append(intervals[i])
            #if it is an overlapping interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        results.append(newInterval)

        return results