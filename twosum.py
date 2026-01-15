from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0,0]


def test_example_1():
    nums = [2,7,11,15]
    target = 9
    assert Solution().twoSum(nums, target) == [0,1]

def test_example_2():
    nums = [3,2,4]
    target = 6
    assert Solution().twoSum(nums, target) == [1,2]

def test_example_3():
    nums = [3,3]
    target = 6
    assert Solution().twoSum(nums, target) == [0,1]
