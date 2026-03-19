from typing import List


class Solution:
    DIGITS_TO_LETTERS = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        def findRecursive(combo, i):
            if i == len(digits):
                ans.append(''.join(combo))
                return

            for letter in Solution.DIGITS_TO_LETTERS[digits[i]]:
                combo.append(letter)
                findRecursive(combo, i + 1)
                combo.pop()

        ans = []
        findRecursive([], 0)
        return ans


def test_example_1():
    digits = "23"
    answer = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(Solution().letterCombinations(digits)) == sorted(answer)


def test_example_2():
    digits = "2"
    answer = ["a", "b", "c"]
    assert sorted(Solution().letterCombinations(digits)) == sorted(answer)
