from collections import defaultdict
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occurrences = defaultdict(int)
        for num in nums:
            occurrences[num] += 1

        largest = -1
        for num, count in occurrences.items():
            if count == 1 and num > largest:
                largest = num

        return largest


def test_example_1():
    nums = [5,7,3,9,4,9,8,3,1]
    assert Solution().largestUniqueNumber(nums) == 8

def test_example_2():
    nums = [9,9,8,8]
    assert Solution().largestUniqueNumber(nums) == -1
