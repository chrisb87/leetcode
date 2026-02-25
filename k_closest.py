from heapq import heappush, heappop
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heappush(heap, (-distance, x, y))
            if len(heap) > k:
                heappop(heap)
        return [[x, y] for distance, x, y in heap]


def test_example_1():
    points = [[1, 3], [-2, 2]]
    k = 1
    answer = [[-2, 2]]
    assert sorted(Solution().kClosest(points, k)) == sorted(answer)


def test_example_2():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    answer = [[3, 3], [-2, 4]]
    assert sorted(Solution().kClosest(points, k)) == sorted(answer)
