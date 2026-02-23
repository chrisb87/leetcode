import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(i: int) -> int:
            detonations = 1
            x1, y1, r = bombs[i]
            for j in range(len(bombs)):
                if j not in seen:
                    x2, y2, _ = bombs[j]
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    if distance <= r:
                        seen.add(j)
                        detonations += dfs(j)
            return detonations

        answer = 0

        for i in range(len(bombs)):
            seen = {i}
            answer = max(answer, dfs(i))

        return answer


def test_example_1():
    bombs = [[2, 1, 3], [6, 1, 4]]
    assert Solution().maximumDetonation(bombs) == 2


def test_example_2():
    bombs = [[1, 1, 5], [10, 10, 5]]
    assert Solution().maximumDetonation(bombs) == 1


def test_example_3():
    bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    assert Solution().maximumDetonation(bombs) == 5
