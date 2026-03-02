from typing import List


class Solution:
    def answerWithPsum(self, psum: List[int], query: int):
        left = 0
        right = len(psum) - 1
        while left <= right:
            mid = (left + right) // 2
            if psum[mid] == query:
                return mid + 1
            elif psum[mid] < query:
                left = mid + 1
            elif psum[mid] > query:
                right = mid - 1
        return left

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        psum = []
        for num in sorted(nums):
            if len(psum) == 0:
                psum.append(num)
            else:
                psum.append(num + psum[-1])

        answers = []

        for query in queries:
            answers.append(self.answerWithPsum(psum, query))

        return answers


def test_example_1():
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    answer = [2, 3, 4]
    assert Solution().answerQueries(nums, queries) == answer


def test_example_2():
    nums = [2, 3, 4, 5]
    queries = [1]
    answer = [0]
    assert Solution().answerQueries(nums, queries) == answer
