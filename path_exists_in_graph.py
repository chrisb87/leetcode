from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(source: int, destination: int) -> bool:
            if source == destination:
                return True

            for neighbor in graph[source]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor, destination):
                        return True

            return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set([source])
        return dfs(source, destination)


def test_example_1():
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    assert Solution().validPath(n, edges, source, destination) == True


def test_example_2():
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    assert Solution().validPath(n, edges, source, destination) == False
