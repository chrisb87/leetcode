from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node: int):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        answer = 0

        for i in range(n):
            if i not in seen:
                seen.add(i)
                answer += 1
                dfs(i)

        return answer


def test_example_1():
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert Solution().countComponents(n, edges) == 2


def test_example_2():
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert Solution().countComponents(n, edges) == 1
