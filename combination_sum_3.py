from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def recurse(path: List[int]):
            print(f"recurse with path {path}")

            if len(path) == k:
                print(f"\tlen is k")
                if sum(path) == n:
                    print(f"\t\tsum is n")
                    ans.append(path[:])
                return

            for i in range(1, 10):
                if i not in path:
                    path.append(i)
                    if sum(path) <= n:
                        recurse(path)
                    path.pop()

        ans = []
        for i in range(1, 10):
            recurse([i])
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
    assert sorted(Solution().combinationSum3(k, n)) == sorted(answer)


def test_example_3():
    k = 4
    n = 1
    answer = []
    assert sorted(Solution().combinationSum3(k, n)) == sorted(answer)
