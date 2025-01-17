class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval
        
        for i in intervals:
            if i[1] < start:
                res.append(i)
            elif i[0] > end:
                res.append([start, end])
                return res + intervals[intervals.index(i):]
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        
        res.append([start, end])
        return res