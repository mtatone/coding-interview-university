import heapq, math


class Solution:
    @staticmethod
    def kClosest(points, k):
        res = []
        heap = {}
        for point in points:
            distance = math.sqrt((point[0] ** 2 + point[1] ** 2))
            heap[distance] = point
        heapq._heapify_max(heap)
        for i in range(k):
            res.append(heapq._heappop_max(heap))
        return res


res = Solution.kClosest(points=[[1,3],[-2,2]], k=1)
print(res)
