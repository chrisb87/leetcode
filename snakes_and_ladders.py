from collections import defaultdict, deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def boustrophedon_number_to_board_value(n: int) -> int:
            row = int((n - 1) / cols)
            brow = -1 - row

            col = (n % cols) - 1
            if row % 2 == 1:
                col = -1 - col

            return board[brow][col]

        rows = len(board)
        cols = len(board[0])
        target = rows * cols
        seen = defaultdict(lambda: float("inf"))  # n => min_rolls
        queue = deque([(1, 0)])  # n, rolls

        while queue:
            curr, rolls = queue.popleft()

            for progress in range(1, 7):
                new_curr = min(target, curr + progress)
                new_rolls = rolls + 1

                board_value = boustrophedon_number_to_board_value(new_curr)
                if board_value != -1:
                    new_curr = board_value

                if new_curr == target:
                    return new_rolls

                if seen[new_curr] > new_rolls:
                    seen[new_curr] = new_rolls
                    queue.append((new_curr, new_rolls))

        return -1


def test_example_1():
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    assert Solution().snakesAndLadders(board) == 4


def test_example_2():
    board = [[-1, -1],
             [-1, 3]]
    assert Solution().snakesAndLadders(board) == 1


def test_failure_1():
    board = [[-1, -1, -1],
             [-1, 9, 8],
             [-1, 8, 9]]
    assert Solution().snakesAndLadders(board) == 1


def test_failure_2():
    board = [[1, 1, -1],
             [1, 1, 1],
             [-1, 1, 1]]
    assert Solution().snakesAndLadders(board) == -1


def test_failure_3():
    board = [[-1, 1, 2, -1],
             [2, 13, 15, -1],
             [-1, 10, -1, -1],
             [-1, 6, 2, 8]]
    assert Solution().snakesAndLadders(board) == 2
