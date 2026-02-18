from typing import List


class Solution:
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValid(row: int, col: int) -> bool:
            return (0 <= row < rows) and (0 <= col < cols) and grid[row][col] == 1

        def areaOfIsland(row: int, col: int, areaSoFar: int = 0) -> int:
            seen.add((row, col))
            areaSoFar += 1
            for dRow, dCol in self.DIRECTIONS:
                nextRow, nextCol = row + dRow, col + dCol
                if isValid(nextRow, nextCol) and (nextRow, nextCol) not in seen:
                    areaSoFar += areaOfIsland(nextRow, nextCol)
            return areaSoFar

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if isValid(row, col) and (row, col) not in seen:
                    islandArea = areaOfIsland(row, col)
                    maxArea = max(islandArea, maxArea)
        return maxArea


def test_example_1():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(grid) == 6


def test_example_2():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(grid) == 0
