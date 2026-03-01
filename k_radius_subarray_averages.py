from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix_sum = []
        for num in nums:
            if len(prefix_sum) == 0:
                prefix_sum.append(num)
            else:
                prefix_sum.append(num + prefix_sum[-1])

        answer = []
        for i in range(len(nums)):
            if (i - k) < 0 or (i + k) >= len(nums):
                answer.append(-1)
            else:
                high_sum = prefix_sum[i+k]
                if i - k - 1 < 0:
                    low_sum = 0
                else:
                    low_sum = prefix_sum[i - k - 1]

                average = (high_sum - low_sum) / ((2 * k) + 1)
                answer.append(int(average))

        return answer


def test_example_1():
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    answer = [-1, -1, -1, 5, 4, 4, -1, -1, -1]
    assert Solution().getAverages(nums, k) == answer


def test_example_2():
    nums = [100000]
    k = 0
    answer = [100000]
    assert Solution().getAverages(nums, k) == answer


def test_example_3():
    nums = [8]
    k = 100000
    answer = [-1]
    assert Solution().getAverages(nums, k) == answer
