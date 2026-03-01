from typing import List


class Solution:
    BASKET_MAX = 5000

    def maxNumberOfApples(self, weight: List[int]) -> int:
        total_weight = 0
        apples = 0
        for w in sorted(weight):
            total_weight += w
            if total_weight > self.BASKET_MAX:
                return apples
            apples += 1
        return apples


def test_example_1():
    weight = [100, 200, 150, 1000]
    answer = 4
    assert Solution().maxNumberOfApples(weight) == answer


def test_example_1():
    weight = [900, 950, 800, 1000, 700, 800]
    answer = 5
    assert Solution().maxNumberOfApples(weight) == answer


def test_failure_1():
    weight = [1000, 1000, 1000, 1000, 1000]
    answer = 5
    assert Solution().maxNumberOfApples(weight) == answer
