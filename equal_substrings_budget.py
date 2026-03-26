# You are given two strings s and t of the same length and an integer maxCost.
#
# You want to change s to t. Changing the ith character of s to ith character of
# t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
#
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding
# substring of t with a cost less than or equal to maxCost. If there is no substring from
# that can be changed to its corresponding substring from t, return 0.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        left = 0
        ans = 0
        curr = 0
        for right in range(len(s)):
            curr += costs[right]
            while curr > maxCost:
                curr -= costs[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


def test_example_1():
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    answer = 3
    assert Solution().equalSubstring(s, t, maxCost) == answer


def test_example_2():
    s = "abcd"
    t = "cdef"
    maxCost = 3
    answer = 1
    assert Solution().equalSubstring(s, t, maxCost) == answer


def test_example_3():
    s = "abcd"
    t = "acde"
    maxCost = 0
    answer = 1
    assert Solution().equalSubstring(s, t, maxCost) == answer
