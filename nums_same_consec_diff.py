from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def recurse(path):
            if len(path) == n:
                ans.append(int(''.join([str(d) for d in path])))
                return

            next_digit = set()

            if path[-1] + k < 10:
                next_digit.add(path[-1] + k)
            if path[-1] - k >= 0:
                next_digit.add(path[-1] - k)

            for digit in next_digit:
                path.append(digit)
                recurse(path)
                path.pop()

        ans = []
        for i in range(1, 10):
            recurse([i])
        return ans


def test_example_1():
    n = 3
    k = 7
    answer = [181, 292, 707, 818, 929]
    assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(answer)


def test_example_2():
    n = 2
    k = 1
    answer = [10, 12, 21, 23, 32, 34, 43, 45,
              54, 56, 65, 67, 76, 78, 87, 89, 98]
    assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(answer)


def test_failure_1():
    n = 2
    k = 0
    answer = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(answer)
