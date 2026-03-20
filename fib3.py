class Fibonacci:
    def __init__(self):
        self.memo = {
            0: 0,
            1: 1
        }

    def get(self, n: int):
        if n not in self.memo:
            self.memo[n] = self.get(n - 2) + self.get(n - 1)
        return self.memo[n]


def test_fib():
    fibonacci = Fibonacci()

    assert fibonacci.get(0) == 0
    assert fibonacci.get(1) == 1
    assert fibonacci.get(2) == 1
    assert fibonacci.get(3) == 2
    assert fibonacci.get(4) == 3
    assert fibonacci.get(5) == 5
    assert fibonacci.get(6) == 8
    assert fibonacci.get(7) == 13
    assert fibonacci.get(8) == 21

    assert fibonacci.get(4) == 3
    assert fibonacci.get(8) == 21
    assert fibonacci.get(0) == 0
    assert fibonacci.get(3) == 2
