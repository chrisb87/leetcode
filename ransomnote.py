# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return False


def test_example_1():
    ransomNote = "a"
    magazine = "b"
    assert Solution().canConstruct(ransomNote, magazine) == False

def test_example_2():
    ransomNote = "aa"
    magazine = "ab"
    assert Solution().canConstruct(ransomNote, magazine) == False

def test_example_3():
    ransomNote = "aa"
    magazine = "aab"
    assert Solution().canConstruct(ransomNote, magazine) == True
