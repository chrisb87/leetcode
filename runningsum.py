from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []

        sum = 0
        for num in nums:
            sum += num
            answer.append(sum)

        return answer



def test_example_1():
    nums = [1,2,3,4]
    expected = [1,3,6,10]
    assert Solution().runningSum(nums) == expected

def test_example_2():
    nums = [1,1,1,1,1]
    expected = [1,2,3,4,5]
    assert Solution().runningSum(nums) == expected

def test_example_3():
    nums = [3,1,2,10,1]
    expected = [3,4,6,16,17]
    assert Solution().runningSum(nums) == expected
