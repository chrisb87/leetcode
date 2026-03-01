class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = [n for n in str(num)]
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
        return int(''.join(digits))


def test_example_1():
    num = 9669
    ans = 9969
    assert Solution().maximum69Number(num) == ans


def test_example_2():
    num = 9996
    ans = 9999
    assert Solution().maximum69Number(num) == ans


def test_example_3():
    num = 9999
    ans = 9999
    assert Solution().maximum69Number(num) == ans
