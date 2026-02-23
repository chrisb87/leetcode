from collections import deque
from typing import List


class Solution:
    def isSingleMutation(self, curr: str, mutation: str):
        mutations = 0

        for i in range(len(curr)):
            if curr[i] != mutation[i]:
                mutations += 1
                if mutations > 1:
                    return False

        return mutations == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_remaining = set(bank)
        queue = deque([startGene])
        mutations = -1

        while queue:
            this_level = len(queue)
            mutations += 1
            for _ in range(this_level):
                curr = queue.popleft()

                if curr == endGene:
                    return mutations

                mutations_to_remove = []
                for mutation in bank_remaining:
                    if self.isSingleMutation(curr, mutation):
                        mutations_to_remove.append(mutation)
                        queue.append(mutation)

                for mutation in mutations_to_remove:
                    bank_remaining.remove(mutation)

        return -1


def test_example_1():
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    assert Solution().minMutation(startGene, endGene, bank) == 1


def test_example_2():
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert Solution().minMutation(startGene, endGene, bank) == 2


def test_failure_1():
    startGene = "AAAAAAAA"
    endGene = "CCCCCCCC"
    bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC",
            "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]
    assert Solution().minMutation(startGene, endGene, bank) == -1
