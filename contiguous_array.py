# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = defaultdict(int) # count -> (first) index where encountered
        counts[0] = -1 # initial count (at -1 index) is 0

        count = 0
        answer = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            elif num == 1:
                count += 1

            if count in counts:
                answer = max(answer, i - counts[count])
            else:
                counts[count] = i

        return answer


def test_example_1():
    nums = [0,1]
    assert Solution().findMaxLength(nums) == 2

def test_example_2():
    nums = [0,1,0]
    assert Solution().findMaxLength(nums) == 2

def test_example_3():
    nums = [0,1,1,1,1,1,0,0,0]
    assert Solution().findMaxLength(nums) == 6
