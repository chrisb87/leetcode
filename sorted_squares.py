from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([n * n for n in nums])
    


def test_example_1():
    nums = [-4,-1,0,3,10]
    expected = [0,1,9,16,100]
    assert sortedSquares(nums) == expected


def test_example_2():
    nums = [-7,-3,2,3,11]
    expected = [4,9,9,49,121]
    assert sortedSquares(nums) == expected

