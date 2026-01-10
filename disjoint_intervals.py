import bisect

class SummaryRanges:

    def __init__(self):
        pass

    def addNum(self, value: int) -> None:
        pass

    def getIntervals(self) -> List[List[int]]:
        pass


class test_example_1():
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
