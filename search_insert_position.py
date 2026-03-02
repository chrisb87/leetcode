from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


def test_example_1():
    nums = [1, 3, 5, 6]
    target = 5
    answer = 2
    assert Solution().searchInsert(nums, target) == answer


def test_example_2():
    nums = [1, 3, 5, 6]
    target = 2
    answer = 1
    assert Solution().searchInsert(nums, target) == answer


def test_example_3():
    nums = [1, 3, 5, 6]
    target = 7
    answer = 4
    assert Solution().searchInsert(nums, target) == answer
