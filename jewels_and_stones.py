# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        answer = 0
        for s in stones:
            if s in jewelSet:
                answer += 1
        return answer



def test_example_1():
    jewels = "aA"
    stones = "aAAbbbb"
    assert Solution().numJewelsInStones(jewels, stones) == 3

def test_example_2():
    jewels = "z"
    stones = "ZZ"
    assert Solution().numJewelsInStones(jewels, stones) == 0
