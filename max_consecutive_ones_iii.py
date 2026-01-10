from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        answer = 0
        left = 0
        curr_zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr_zeros += 1
            while(curr_zeros > k):
                if nums[left] == 0:
                    curr_zeros -= 1
                left += 1
            length = right - left + 1
            if length > answer:
                answer = length
        
        return answer


def test_example_1():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    assert Solution().longestOnes(nums, k) == 6

def test_example_2():
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    assert Solution().longestOnes(nums, k) == 10
