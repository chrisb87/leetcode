from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            stick1, stick2 = heappop(sticks), heappop(sticks)
            combined = stick1 + stick2
            cost += combined
            heappush(sticks, combined)
        return cost


def test_example_1():
    sticks = [2, 4, 3]
    assert Solution().connectSticks(sticks) == 14


def test_example_2():
    sticks = [1, 8, 3, 5]
    assert Solution().connectSticks(sticks) == 30


def test_example_3():
    sticks = [5]
    assert Solution().connectSticks(sticks) == 0
