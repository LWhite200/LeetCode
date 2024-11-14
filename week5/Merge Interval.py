class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0]) # we merge accourding to the first value
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1] # [most resent][second value]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output