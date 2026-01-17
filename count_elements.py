from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        answer = 0
        arr_set = set(arr)
        for element in arr:
            if element + 1 in arr_set:
                answer += 1
        return answer


def test_example_1():
    arr = [1,2,3]
    assert Solution().countElements(arr) == 2

def test_example_2():
    arr = [1,1,3,3,5,5,7,7]
    assert Solution().countElements(arr) == 0
