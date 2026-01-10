from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    ans = []

    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            break
        i += 1

    j = i + 1

    while i >= 0 and j < len(nums):
        i_squared = nums[i] * nums[i]
        j_squared = nums[j] * nums[j]

        if i_squared < j_squared:
            ans.append(i_squared)
            i -= 1
        else:
            ans.append(j_squared)
            j += 1

    while i >= 0:
        i_squared = nums[i] * nums[i]
        ans.append(i_squared)
        i -= 1

    while j < len(nums):
        j_squared = nums[j] * nums[j]
        ans.append(j_squared)
        j += 1

    return ans
    


def test_example_1():
    nums = [-4,-1,0,3,10]
    expected = [0,1,9,16,100]
    assert sortedSquares(nums) == expected


def test_example_2():
    nums = [-7,-3,2,3,11]
    expected = [4,9,9,49,121]
    assert sortedSquares(nums) == expected

