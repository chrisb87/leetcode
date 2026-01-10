from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        j = 0
        while j < len(nums):
            if nums[j] >= 0:
                break
            j += 1

        i = j - 1

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
            try:
                i_squared = nums[i] * nums[i]
            except:
                import pdb; pdb.set_trace()
                
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
    assert Solution().sortedSquares(nums) == expected


def test_example_2():
    nums = [-7,-3,2,3,11]
    expected = [4,9,9,49,121]
    assert Solution().sortedSquares(nums) == expected


def test_failure_1():
    nums = [-1]
    expected = [1]
    assert Solution().sortedSquares(nums) == expected
