class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            mHeap.append((dist, x, y))

        heapq.heapify(mHeap)
        res = []
        for i in range(k):
            i, x, y = heapq.heappop(mHeap)
            res.append((x, y))
        return res