def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    print(f"n = {n}")

    return fib(n - 2) + fib (n - 1)


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21

    assert fib(4) == 3
    assert fib(8) == 21
    assert fib(0) == 0
    assert fib(3) == 2
