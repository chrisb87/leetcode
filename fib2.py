class Fibonacci:
    def __init__(self):
        self.sequence = [0,1]

    def get(self, n: int):
        while len(self.sequence) <= n:
            next_fib = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_fib)

        return self.sequence[n]


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
