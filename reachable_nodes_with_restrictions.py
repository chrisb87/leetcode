from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node: int):
            nonlocal reachable_nodes
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    seen.add(neighbor)
                    reachable_nodes += 1
                    dfs(neighbor)

        restricted = set(restricted)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set([0])
        reachable_nodes = 1
        dfs(0)
        return reachable_nodes


def test_example_1():
    n = 7
    edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
    restricted = [4, 5]
    assert Solution().reachableNodes(n, edges, restricted) == 4


def test_example_2():
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    assert Solution().reachableNodes(n, edges, restricted) == 3
