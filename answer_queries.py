from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []

        for query in queries:
            sum = 0
            count = 0

            for num in nums:
                sum += num
                count += 1
                if sum > query:
                    count -= 1
                    break

            answer.append(count)

        return answer


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
