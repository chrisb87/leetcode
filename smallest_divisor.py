from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def test(divisor):
            return sum([ceil(n / divisor) for n in nums]) <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if test(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


def test_example_1():
    nums = [1, 2, 5, 9]
    threshold = 6
    answer = 5
    assert Solution().smallestDivisor(nums, threshold) == answer


def test_example_2():
    nums = [44, 22, 33, 11, 1]
    threshold = 5
    answer = 44
    assert Solution().smallestDivisor(nums, threshold) == answer
