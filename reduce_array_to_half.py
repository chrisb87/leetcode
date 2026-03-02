from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        curr_size = len(arr)
        target = int(curr_size / 2)
        answer = 0
        counts = Counter(arr)
        for n, count in sorted([(k, v) for (k, v) in Counter(arr).items()], key=lambda i: i[1], reverse=True):
            curr_size -= count
            answer += 1
            if curr_size <= target:
                return answer
        return answer


def test_example_1():
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    answer = 2
    assert Solution().minSetSize(arr) == answer


def test_example_2():
    arr = [7, 7, 7, 7, 7, 7]
    answer = 1
    assert Solution().minSetSize(arr) == answer
