"""
Day 63: Dynamic Programming (LCS, Subsets, Knapsack)
"""

from typing import List


# ---------------------------------------------------------
# Problem: Partition Equal Subset Sum (LeetCode 416, Medium)
# Link: https://leetcode.com/problems/partition-equal-subset-sum/
# ---------------------------------------------------------
class Solution416:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]
        return dp[target]


# ---------------------------------------------------------
# Problem: Longest Palindromic Subsequence (LeetCode 516, Medium)
# Link: https://leetcode.com/problems/longest-palindromic-subsequence/
# ---------------------------------------------------------
class Solution516:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


# ---------------------------------------------------------
# Problem: Profitable Schemes (LeetCode 879, Hard)
# Link: https://leetcode.com/problems/profitable-schemes/
# ---------------------------------------------------------
class Solution879:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        MOD = 10**9 + 7
        m = len(group)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for idx in range(m):
            g = group[idx]
            p = profit[idx]
            for j in range(n, g - 1, -1):
                for old_p in range(minProfit + 1):
                    if dp[j - g][old_p]:
                        new_p = old_p + p
                        if new_p > minProfit:
                            new_p = minProfit
                        dp[j][new_p] = (dp[j][new_p] + dp[j - g][old_p]) % MOD

        return sum(dp[j][minProfit] for j in range(n + 1)) % MOD


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("LeetCode 416 Example:", Solution416().canPartition([1, 5, 11, 5]))
    print("LeetCode 516 Example:", Solution516().longestPalindromeSubseq("bbbab"))
    print(
        "LeetCode 879 Example:", Solution879().profitableSchemes(5, 3, [2, 2], [2, 3])
    )
