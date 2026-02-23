from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = {start}

        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True

            for next_i in (i + arr[i], i - arr[i]):
                if next_i not in seen and 0 <= next_i < len(arr):
                    seen.add(next_i)
                    queue.append(next_i)

        return False


def test_example_1():
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    assert Solution().canReach(arr, start) == True


def test_example_2():
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 0
    assert Solution().canReach(arr, start) == True


def test_example_3():
    arr = [3, 0, 2, 1, 2]
    start = 2
    assert Solution().canReach(arr, start) == False
