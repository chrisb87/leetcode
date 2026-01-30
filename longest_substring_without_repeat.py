# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        curr_chars = set()
        left = 0
        
        for right in range(0, len(s)):
            while s[right] in curr_chars:
                curr_chars.remove(s[left])
                left += 1
            curr_chars.add(s[right])
            answer = max(answer, len(curr_chars))

        return answer


def test_example_1():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 3

def test_example_2():
    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring(s) == 1

def test_example_3():
    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring(s) == 3 # "wke"
