class Solution:
    LETTER_PAIRINGS = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'H',
        'i': 'I',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'p': 'P',
        'q': 'Q',
        'r': 'R',
        's': 'S',
        't': 'T',
        'u': 'U',
        'v': 'V',
        'w': 'W',
        'x': 'X',
        'y': 'Y',
        'z': 'Z',

        'A': 'a',
        'B': 'b',
        'C': 'c',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'H': 'h',
        'I': 'i',
        'J': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'O': 'o',
        'P': 'p',
        'Q': 'q',
        'R': 'r',
        'S': 's',
        'T': 't',
        'U': 'u',
        'V': 'v',
        'W': 'w',
        'X': 'x',
        'Y': 'y',
        'Z': 'z',
    }

    def makeGood(self, s: str) -> str:
        stack = []

        for letter in s:
            if len(stack) >= 1 and letter == self.LETTER_PAIRINGS[stack[-1]]:
                stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)
    
def test_example_1():
    s = "leEeetcode"
    solution = "leetcode"
    assert Solution().makeGood(s) == solution

def test_example_2():
    s = "abBAcC"
    solution = ""
    assert Solution().makeGood(s) == solution

def test_example_3():
    s = "s"
    solution = "s"
    assert Solution().makeGood(s) == solution
