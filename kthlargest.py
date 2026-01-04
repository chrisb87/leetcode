from typing import List
import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[0 - self.k:]

    def add(self, val: int) -> int:
        if len(self.nums) < self.k or val >= self.nums[0]:
            bisect.insort(self.nums, val)
            self.nums = self.nums[0 - self.k:]
        return self.nums[0]


def test_example_1():
    kthlargest = KthLargest(3, [4, 5, 8, 2])
    assert kthlargest.add(3) == 4
    assert kthlargest.add(5) == 5
    assert kthlargest.add(10) == 5
    assert kthlargest.add(9) == 8
    assert kthlargest.add(4) == 8

def test_example_2():
    kthlargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert kthlargest.add(2) == 7
    assert kthlargest.add(10) == 7
    assert kthlargest.add(9) == 7
    assert kthlargest.add(9) == 8
