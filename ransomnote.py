# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


from collections import defaultdict

 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineChars = defaultdict(int)
        for c in magazine:
            magazineChars[c] += 1

        ransomNoteChars = defaultdict(int)
        for c in ransomNote:
            ransomNoteChars[c] += 1

        for c in ransomNoteChars:
            if magazineChars[c] < ransomNoteChars[c]:
                return False

        return True


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
