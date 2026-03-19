from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def findPaths(path: List[int]):
            if path[-1] == len(graph) - 1:
                ans.append(path[:])
                return

            for edge in graph[path[-1]]:
                path.append(edge)
                findPaths(path)
                path.pop()

        ans = []
        findPaths([0])
        return ans


def test_example_1():
    graph = [[1, 2], [3], [3], []]
    answer = [[0, 1, 3], [0, 2, 3]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(answer)


def test_example_2():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    answer = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(answer)
