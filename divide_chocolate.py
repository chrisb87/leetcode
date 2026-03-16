from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def test(min_sweetness):
            chunks = 0
            curr = 0
            for i in range(len(sweetness)):
                curr += sweetness[i]
                if curr >= min_sweetness:
                    chunks += 1
                    curr = 0
                    if chunks == k + 1:
                        return True
            return False

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)

        while left < right:
            mid = (left + right + 1) // 2
            if test(mid):
                left = mid
            else:
                right = mid - 1

        return left


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


def test_example_3():
    sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
    k = 2
    answer = 5
    assert Solution().maximizeSweetness(sweetness, k) == answer
