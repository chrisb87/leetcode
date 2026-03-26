class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        curr_vowels = 0
        left = 0
        for right in range(len(s)):
            if s[right] in self.VOWELS:
                curr_vowels += 1
            if right - left + 1 == k:
                ans = max(ans, curr_vowels)
                if s[left] in self.VOWELS:
                    curr_vowels -= 1
                left += 1

        return ans


def test_example_1():
    s = "abciiidef"
    k = 3
    answer = 3
    assert Solution().maxVowels(s, k) == answer


def test_example_2():
    s = "aeiou"
    k = 2
    answer = 2
    assert Solution().maxVowels(s, k) == answer


def test_example_3():
    s = "leetcode"
    k = 3
    answer = 2
    assert Solution().maxVowels(s, k) == answer
