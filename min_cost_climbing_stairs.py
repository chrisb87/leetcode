from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recurse_min_cost(i):
            if i not in memo:
                memo[i] = min(recurse_min_cost(i - 1) + cost[i-1],
                              recurse_min_cost(i - 2) + cost[i-2])
            return memo[i]

        memo = {0: 0, 1: 0}
        return recurse_min_cost(len(cost))


def test_example_1():
    cost = [10, 15, 20]
    answer = 15
    assert Solution().minCostClimbingStairs(cost) == answer


def test_example_2():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    answer = 6
    assert Solution().minCostClimbingStairs(cost) == answer
