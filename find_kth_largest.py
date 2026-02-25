from heapq import heappush, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert Solution().findKthLargest(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert Solution().findKthLargest(nums, k) == 4
