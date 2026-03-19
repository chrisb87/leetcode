from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recurse(path, l_used, r_used):
            if l_used == n and r_used == n:
                ans.append(''.join(path))
                return

            if l_used < n:
                path.append('(')
                recurse(path, l_used + 1, r_used)
                path.pop()

            if r_used < n and r_used < l_used:
                path.append(')')
                recurse(path, l_used, r_used + 1)
                path.pop()

        ans = []
        recurse([], 0, 0)
        return ans


def test_example_1():
    n = 3
    answer = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(Solution().generateParenthesis(n)) == sorted(answer)


def test_example_2():
    n = 1
    answer = ["()"]
    assert sorted(Solution().generateParenthesis(n)) == sorted(answer)
