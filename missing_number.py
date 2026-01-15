from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest = None
        seen = set()

        for num in nums:
            if largest == None or num > largest:
                largest = num
            seen.add(num)

        if largest != None:
            for i in range(0, largest):
                if i not in seen:
                    return i
            return largest + 1
        return nums[0] + 1


def test_example_1():
    nums = [3,0,1]
    assert Solution().missingNumber(nums) == 2

def test_example_2():
    nums = [0,1]
    assert Solution().missingNumber(nums) == 2

def test_example_3():
    nums = [9,6,4,2,3,5,7,0,1]
    assert Solution().missingNumber(nums) == 8

def test_error_1():
    nums = [0]
    assert Solution().missingNumber(nums) == 1

def test_error_2():
    nums = [1]
    assert Solution().missingNumber(nums) == 0
