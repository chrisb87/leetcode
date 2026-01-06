from typing import List

class StreamChecker:
    def __init__(self, words: List[str]):
        self.max_word_len = max([len(word) for word in words])
        self.stream = ""
        self.words_trie = TrieNode()
        for word in words:
            self.words_trie.insert(word)

    def query(self, letter: str) -> bool:
        self.stream += letter
        if len(self.stream) > self.max_word_len:
            self.stream = self.stream[0 - self.max_word_len:]

        for word_len in range(self.max_word_len):
            suffix = self.stream[-1 - word_len:]
            
            if self.words_trie.search(suffix):
                return True

        return False


class TrieNode:
    character_to_index = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}

    def __init__(self):
        self.children = [None] * len(self.character_to_index)
        self.isEndOfWord = False

    def insert(self, word: str):
        character = word[0]
        character_index = self.character_to_index[character]

        if self.children[character_index] == None:
            self.children[character_index] = TrieNode()

        if len(word) == 1:
            self.children[character_index].isEndOfWord = True
        else:
            self.children[character_index].insert(word[1:])

    def search(self, word: str) -> bool:
        character = word[0]
        character_index = self.character_to_index[character]

        if self.children[character_index] == None:
            return False
        
        if self.children[character_index].isEndOfWord and len(word) == 1:
            if len(word) == 1:
                return True
            
        if len(word) == 1:
            return False
        else:
            return self.children[character_index].search(word[1:])



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


def test_case_2():
    streamChecker = StreamChecker(["ab","ba","aaab","abab","baa"])
    assert streamChecker.query("a") == False
    assert streamChecker.query("a") == False
    assert streamChecker.query("a") == False
    assert streamChecker.query("a") == False
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("b") == False
    assert streamChecker.query("b") == False
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("b") == False
    assert streamChecker.query("b") == False
    assert streamChecker.query("b") == False
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("a") == False
    assert streamChecker.query("b") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("a") == True
    assert streamChecker.query("a") == False
