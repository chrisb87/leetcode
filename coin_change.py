from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def backtrack(counts: List[int]):
            print(f"backtrack {counts}")
            nonlocal ans
            if sum([counts[i] * coins[i] for i in range(len(coins))]) == amount:
                ans = sum(counts)

            for i in reversed(range(len(coins))):
                counts[i] += 1
                print(f"trying counts {counts}")
                total = sum([counts[i] * coins[i] for i in range(len(coins))])
                if total == amount:
                    ans = sum(counts)
                    print(f"new answer {ans} with counts {counts}")
                    return
                elif total < amount:
                    backtrack(counts)
                    counts[i] -= 1
                elif total > amount:
                    print(f"exceed total")
                    counts[i] -= 1
                    next

        coins.sort()
        print(f"coins {coins}")
        counts = [0 for _ in range(len(coins))]
        #ans = -1
        #backtrack(counts)
        #return ans
    
        # each coin
        total = 0
        for i in reversed(range(len(coins))):
            while total < amount:
                counts[i] += 1
                total = sum([counts[i] * coins[i] for i in range(len(coins))])
                if total == amount:
                    return sum(counts)
                elif total > amount:
                    counts[i] -= 1


def test_example_1():
    coins = [1, 2, 5]
    amount = 11
    answer = 3
    assert Solution().coinChange(coins, amount) == answer


def test_example_2():
    coins = [2]
    amount = 3
    answer = -1
    assert Solution().coinChange(coins, amount) == answer


def test_example_3():
    coins = [1]
    amount = 0
    answer = 0
    assert Solution().coinChange(coins, amount) == answer
