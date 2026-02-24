from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def singleLetterDifference(word1: str, word2: str) -> bool:
            differences = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences == 1

        queue = deque([(beginWord, 0)])
        seen = set()
        while queue:
            word, depth = queue.popleft()

            if word == endWord:
                return depth + 1

            for word2 in wordList:
                if word2 not in seen and singleLetterDifference(word, word2):
                    seen.add(word2)
                    queue.append((word2, depth + 1))

        return 0


def test_example_1():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 5


def test_example_2():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    assert Solution().ladderLength(beginWord, endWord, wordList) == 0
