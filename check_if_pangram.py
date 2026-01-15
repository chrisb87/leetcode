class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for letter in sentence:
            seen.add(letter)
            if len(seen) == 26:
                return True
        return False


def test_example_1():
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    assert Solution().checkIfPangram(sentence) == True

def test_example_2():
    sentence = "leetcode"
    assert Solution().checkIfPangram(sentence) == False

