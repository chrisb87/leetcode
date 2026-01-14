
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        return 0


def test_example_1():
    nums = [10,5,2,6]
    k = 100
    assert Solution().numSubarrayProductLessThanK(nums, k) == 8

def test_example_2():
    nums = [1,2,3]
    k = 0
    assert Solution().numSubarrayProductLessThanK(nums, k) == 0
