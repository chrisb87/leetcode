from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        return 0


def test_example_1():
    sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    answer = 6
    assert Solution().maximizeSweetness(sweetness, k) == answer


def test_example_2():
    sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    k = 8
    answer = 1
    assert Solution().maximizeSweetness(sweetness, k) == answer


def test_example_34():
    sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
    k = 2
    answer = 5
    assert Solution().maximizeSweetness(sweetness, k) == answer
