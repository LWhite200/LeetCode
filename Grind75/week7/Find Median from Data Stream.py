" Finding the median value using a heap "
" I remember seeing this problem months ago "
" I have become good and proud of my python "

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) == 0 or num <= -self.low[0]:
            heapq.heappush(self.low, -num) 
        else:
            heapq.heappush(self.high, num)
            
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.low) + 1 < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))
            

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2.0
        elif len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return self.high[0]  