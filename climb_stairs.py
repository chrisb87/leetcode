from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        costs = [0 for _ in range(n)]
        costs[0] = 1
        costs[1] = 2
        for i in range(2, n):
            costs[i] = costs[i-1] + costs[i-2]
        return costs[n-1]


class Solution2:
    def climbStairs(self, n: int) -> int:
        @cache
        def recurse(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            return recurse(i - 1) + recurse(i - 2)
        return recurse(n)


def test_example_1():
    n = 2
    answer = 2
    assert Solution().climbStairs(n) == answer


def test_example_2():
    n = 3
    answer = 3
    assert Solution().climbStairs(n) == answer


def test_failure_1():
    n = 4
    answer = 5
    assert Solution().climbStairs(n) == answer


def test_failure_2():
    n = 1
    answer = 1
    assert Solution().climbStairs(n) == answer
