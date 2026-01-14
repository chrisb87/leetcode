from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = nums[0]
        minvalue = running_sum

        for i in range(1, len(nums)):
            running_sum += nums[i]
            if running_sum < minvalue:
                minvalue = running_sum

        minvalue = 1 - minvalue
        return max(minvalue, 1)
    

def test_example_1():
    nums = [-3,2,-3,4,2]
    expected = 5
    assert Solution().minStartValue(nums) == expected

def test_example_2():
    nums = [1,2]
    expected = 1
    assert Solution().minStartValue(nums) == expected

def test_example_3():
    nums = [1,-2,-3]
    expected = 5
    assert Solution().minStartValue(nums) == expected

