from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum

        for right in range(k, len(nums)):
            curr_sum += nums[right]
            curr_sum -= nums[right - k]
            if curr_sum > max_sum:
                max_sum = curr_sum


        return max_sum / k
    

def test_max_average():
    nums = [1,12,-5,-6,50,3]
    k = 4
    assert Solution().findMaxAverage(nums, k) == 12.75

def test_wrong_answer():
    nums = [0,1,1,3,3]
    k = 4
    assert Solution().findMaxAverage(nums, k) == 2.0
