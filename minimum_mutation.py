from collections import deque
from typing import List


class Solution:
    BASES = ('A', 'C', 'G', 'T')

    def mutations(self, gene: str):
        for i in range(len(gene)):
            for base in self.BASES:
                if gene[i] == base:
                    continue
                yield gene[:i] + base + gene[i+1:]

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([startGene])
        mutations = -1

        while queue:
            this_level = len(queue)
            mutations += 1
            for _ in range(this_level):
                gene = queue.popleft()

                if gene == endGene:
                    return mutations

                for mutation in self.mutations(gene):
                    if mutation in bank:
                        queue.append(mutation)

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
