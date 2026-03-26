from typing import List

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = float("+inf")
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        if ans == float("+inf"):
            return 0
        return ans


def test_example_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    answer = 2
    assert Solution().minSubArrayLen(target, nums) == answer


def test_example_2():
    target = 4
    nums = [1, 4, 4]
    answer = 1
    assert Solution().minSubArrayLen(target, nums) == answer


def test_example_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    answer = 0
    assert Solution().minSubArrayLen(target, nums) == answer


def test_failure_1():
    target = 11
    nums = [1, 2, 3, 4, 5]
    answer = 3
    assert Solution().minSubArrayLen(target, nums) == answer


def test_failure_2():
    target = 15
    nums = [1, 2, 3, 4, 5]
    answer = 5
    assert Solution().minSubArrayLen(target, nums) == answer


def test_failure_3():
    target = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    answer = 2
    assert Solution().minSubArrayLen(target, nums) == answer

def test_failure_4():
    target = 6
    nums = [10,2,3]
    answer = 1
    assert Solution().minSubArrayLen(target, nums) == answer
