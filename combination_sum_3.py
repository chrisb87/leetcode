from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def recurse(combo: list[int]):
            if len(combo) == k:
                if sum(combo) == n:
                    ans.append(combo[:])
                return

            next_start = 1
            if len(combo) > 0:
                next_start = combo[-1] + 1

            for i in range(next_start, 10):
                combo.append(i)
                if sum(combo) <= n:
                    recurse(combo)
                combo.pop()

        ans = []
        recurse([])
        return ans


def test_example_1():
    k = 3
    n = 7
    answer = [[1, 2, 4]]
    assert sorted(Solution().combinationSum3(k, n)) == sorted(answer)


def test_example_2():
    k = 3
    n = 9
    answer = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    # import pdb; pdb.set_trace()
    print(sorted(Solution().combinationSum3(k, n)))
    assert sorted(Solution().combinationSum3(k, n)) == sorted(answer)


def test_example_3():
    k = 4
    n = 1
    answer = []
    assert sorted(Solution().combinationSum3(k, n)) == sorted(answer)
