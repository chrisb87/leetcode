from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        for _ in range(k):
            pile = heappop(piles)
            pile = pile - int(pile / 2)
            heappush(piles, pile)
        return sum([-pile for pile in piles])


def test_example_1():
    piles = [5, 4, 9]
    k = 2
    assert Solution().minStoneSum(piles, k) == 12


def test_example_2():
    piles = [4, 3, 6, 7]
    k = 3
    assert Solution().minStoneSum(piles, k) == 12
