from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        while len(self.queue) >= self.size:
            self.queue.popleft()

        self.queue.append(val)
        return sum(self.queue) / len(self.queue)


def test_example_1():
    size = 3
    obj = MovingAverage(size)
    assert obj.next(1) == 1.0
    assert obj.next(10) == 5.5
    assert abs(obj.next(3) - 4.666666666667) < 1e-9
    assert obj.next(5) == 6.0
