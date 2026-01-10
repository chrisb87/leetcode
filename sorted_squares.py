from typing import List


def sortedSquares(self, nums: List[int]) -> List[int]:
    return nums


def test_example_1():
    input = [-4,-1,0,3,10]
    output = [0,1,9,16,100]
    assert sortedSquares(input) == output


def test_example_2():
    input = [-7,-3,2,3,11]
    output = [4,9,9,49,121]
    assert sortedSquares(input) == output

