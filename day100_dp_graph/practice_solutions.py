""" 
Day 100: DP / Graph - LeetCode Problem Solutions 
"""
from typing import List

# ---------------------------------------------------------
# Problem: Super Ugly Number (LeetCode 313, Medium)
# Link: https://leetcode.com/problems/super-ugly-number/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, n: int, primes: List[int]) -> int:
        """
        Use multiple pointer DP to generate ugly numbers.
        Each pointer tracks next multiple for each prime.
        """
        ugly = [1]
        k = len(primes)
        idx = [0] * k

        for _ in range(1, n):
            next_val = min(primes[i] * ugly[idx[i]] for i in range(k))
            ugly.append(next_val)

            for i in range(k):
                if primes[i] * ugly[idx[i]] == next_val:
                    idx[i] += 1

        return ugly[-1]


# ---------------------------------------------------------
# Problem: Frog Jump (LeetCode 403, Hard)
# Link: https://leetcode.com/problems/frog-jump/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, stones: List[int]) -> bool:
        """
        DP + Hash Map of possible jumps from each stone.
        For each stone, store jump sizes that can reach it.
        """
        stone_set = set(stones)
        dp = {s: set() for s in stones}
        dp[0].add(0)

        for s in stones:
            for k in dp[s]:
                for step in [k - 1, k, k + 1]:
                    if step > 0 and s + step in stone_set:
                        dp[s + step].add(step)

        return len(dp[stones[-1]]) > 0


# ---------------------------------------------------------
# Problem: Find the Town Judge (LeetCode 997, Easy)
# Link: https://leetcode.com/problems/find-the-town-judge/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, n: int, trust: List[List[int]]) -> int:
        """
        Simple indegree / outdegree check.
        Town judge trusts no one but is trusted by everyone else.
        """
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i

        return -1


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve(10, [2, 3, 5]))
    print("Problem Two Example:", SolutionProblemTwo().solve([0,1,3,5,6,8,12,17]))
    print("Problem Three Example:", SolutionProblemThree().solve(3, [[1,3],[2,3]]))
