from typing import List

class StreamChecker:
    def __init__(self, words: List[str]):
        self.stream = ""
        self.trie = TrieNode()
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.stream += letter

        current_node = self.trie
        for character in reversed(self.stream):
            if character not in current_node.children:
                return False
            if current_node.children[character].start_of_word:
                return True
            current_node = current_node.children[character]

        return False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.start_of_word = False

    def insert(self, word: str):
        character, rest_of_word = word[-1], word[:-1]
        
        if character not in self.children:
            self.children[character] = TrieNode()
        
        if len(word) == 1:
            self.children[character].start_of_word = True
        else:
            self.children[character].insert(rest_of_word)

    @classmethod
    def contains_suffix(cls, start_node, stream) -> bool:
        current_node = start_node
        current_character = stream[-1]

        if current_character not in current_node.children:
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
