from typing import List


class Solution:
    def boustrophedon_number_to_board_value(self, board, rows, cols, n: int) -> tuple[int, int]:
        row = int((n - 1) / cols)
        brow = -1 - row

        col = (n % cols) - 1
        if row % 2 == 1:
            col = -1 - col

        return board[brow][col]

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows = len(board)
        cols = len(board[0])
        return -1

def test_boustrophedon_number_to_index():
    board = [['i', 'j', 'k', 'l'],
             ['h', 'g', 'f', 'e'],
             ['a', 'b', 'c', 'd']]
    rows = len(board)
    cols = len(board[0])
    solution = Solution()

    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 1) == 'a'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 2) == 'b'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 3) == 'c'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 4) == 'd'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 5) == 'e'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 6) == 'f'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 7) == 'g'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 8) == 'h'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 9) == 'i'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 10) == 'j'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 11) == 'k'
    assert solution.boustrophedon_number_to_board_value(board, rows, cols, 12) == 'l'


def test_example_1():
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    assert Solution().snakesAndLadders(board) == 4


def test_example_2():
    board = [[-1, -1], [-1, 3]]
    assert Solution().snakesAndLadders(board) == 1
