from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)

        for winner, loser in matches:
            if winner not in loss_count:
                loss_count[winner] = 0
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []

        for player in sorted(loss_count):
            if loss_count[player] == 0:
                zero_losses.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)

        return [zero_losses, one_loss]


def test_example_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    assert Solution().findWinners(matches) == expected


def test_example_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    assert Solution().findWinners(matches) == expected
