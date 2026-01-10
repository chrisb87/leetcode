import bisect
from typing import List

class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, value: int) -> None:
        bisect.insort(self.nums, value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []

        if len(self.nums) == 0:
            return intervals

        current_interval_left = self.nums[0]
        current_interval_right = self.nums[0]

        for num in self.nums:
            if num == current_interval_right:
                continue
            elif num - 1 == current_interval_right:
                current_interval_right = num
            else:
                intervals.append([current_interval_left, current_interval_right])
                current_interval_left = num
                current_interval_right = num

        intervals.append([current_interval_left, current_interval_right])

        return intervals


def test_example_1():
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    assert summaryRanges.getIntervals() == [[1, 1]]
    summaryRanges.addNum(3)
    assert summaryRanges.getIntervals() == [[1, 1], [3, 3]]
    summaryRanges.addNum(7)
    assert summaryRanges.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)
    assert summaryRanges.getIntervals() == [[1, 3], [7, 7]]
    summaryRanges.addNum(6)
    assert summaryRanges.getIntervals() == [[1, 3], [6, 7]]
