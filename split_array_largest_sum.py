from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def test(min_sum):
            curr_splits = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > min_sum:
                    curr_splits += 1
                    curr_sum = num
                    if curr_splits > k:
                        return False
            return True

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if test(mid):
                right = mid
            else:
                left = mid + 1

        return left


def test_example_1():
    nums = [7, 2, 5, 10, 8]
    k = 2
    answer = 18
    assert Solution().splitArray(nums, k) == answer


def test_example_2():
    nums = [1, 2, 3, 4, 5]
    k = 2
    answer = 9
    assert Solution().splitArray(nums, k) == answer
