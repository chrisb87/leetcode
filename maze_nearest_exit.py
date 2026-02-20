from collections import deque
from typing import List


class Solution:
    EMPTY = '.'
    WALL = '+'
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def validMove(row: int, col: int):
            return 0 <= row < rows and 0 <= col < cols and maze[row][col] == self.EMPTY

        def isExit(row: int, col: int) -> bool:
            if row == entrance[0] and col == entrance[1]:
                return False
            return row == 0 or row == rows - 1 or col == 0 or col == cols - 1

        rows = len(maze)
        cols = len(maze[0])

        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 0)])

        while queue:
            row, col, steps = queue.popleft()

            if isExit(row, col):
                return steps

            for dRow, dCol in self.DIRECTIONS:
                nextRow, nextCol = row + dRow, col + dCol
                if (nextRow, nextCol) not in seen and validMove(nextRow, nextCol):
                    seen.add((nextRow, nextCol))
                    queue.append((nextRow, nextCol, steps + 1))

        return -1


def test_example_1():
    maze = [["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]]
    entrance = [1, 2]
    assert Solution().nearestExit(maze, entrance) == 1


def test_example_2():
    maze = [["+", "+", "+"],
            [".", ".", "."],
            ["+", "+", "+"]]
    entrance = [1, 0]
    assert Solution().nearestExit(maze, entrance) == 2


def test_example_3():
    maze = [[".", "+"]]
    entrance = [0, 0]
    assert Solution().nearestExit(maze, entrance) == -1


def test_failure_1():
    maze = [["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", "+", "."]]
    entrance = [0, 1]
    assert Solution().nearestExit(maze, entrance) == -1
