from typing import List

class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = words
        self.max_word_len = max([len(word) for word in words])
        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream += letter
        if len(self.stream) > self.max_word_len:
            self.stream = self.stream[0 - self.max_word_len:]

        for word in self.words:
            if self.stream[0 - len(word):] == word:
                return True
        return False


def test_example_1():
    streamChecker = StreamChecker(["cd", "f", "kl"])
    assert streamChecker.query("a") == False
    assert streamChecker.query("b") == False
    assert streamChecker.query("c") == False
    assert streamChecker.query("d") == True
    assert streamChecker.query("e") == False
    assert streamChecker.query("f") == True
    assert streamChecker.query("g") == False
    assert streamChecker.query("h") == False
    assert streamChecker.query("i") == False
    assert streamChecker.query("j") == False
    assert streamChecker.query("k") == False
    assert streamChecker.query("l") == True
