from heapq import heappop, heappush
from typing import List

# binary search solution
# 1420ms, beats 8.93%


class SolutionA:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True

                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))

            return False

        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

# A* solution
# time limit exceeded


class SolutionB:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(heights)
        n = len(heights[0])
        target = (m - 1, n - 1)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = {(0, 0, 0)}
        heap = [(0, 0, 0)]

        while heap:
            effort, row, col = heappop(heap)

            if (row, col) == target:
                return effort

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (effort, next_row, next_col) not in seen:
                    next_effort = abs(
                        heights[next_row][next_col] - heights[row][col])
                    path_effort = max(effort, next_effort)
                    seen.add((path_effort, next_row, next_col))
                    heappush(heap, (path_effort, next_row, next_col))


class Solution(SolutionB):
    pass


def test_example_1():
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    answer = 2
    assert Solution().minimumEffortPath(heights) == answer


def test_example_2():
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    answer = 1
    assert Solution().minimumEffortPath(heights) == answer


def test_example_3():
    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
        1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    answer = 0
    assert Solution().minimumEffortPath(heights) == answer
