from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        return 0


def test_example_1():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    assert Solution().longestOnes(nums, k) == 6

def test_example_2():
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    assert Solution().longestOnes(nums, k) == 10
