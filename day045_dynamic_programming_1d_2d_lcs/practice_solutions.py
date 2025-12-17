"""
Day 45: Dynamic Programming (1D, 2D, LCS) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Edit Distance (LeetCode 72, Medium)
# Link: https://leetcode.com/problems/edit-distance/
# ---------------------------------------------------------
class SolutionEditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]


# ---------------------------------------------------------
# Problem 2: Coin Change (LeetCode 322, Medium)
# Link: https://leetcode.com/problems/coin-change/
# ---------------------------------------------------------
class SolutionCoinChange:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# ---------------------------------------------------------
# Problem 3: Delete Operation for Two Strings (LeetCode 583, Medium)
# Link: https://leetcode.com/problems/delete-operation-for-two-strings/
# ---------------------------------------------------------
class SolutionMinDeleteOperations:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = dp[m][n]
        return (m - lcs) + (n - lcs)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Edit Distance Example:", SolutionEditDistance().minDistance("horse", "ros"))
    print("Coin Change Example:", SolutionCoinChange().coinChange([1, 2, 5], 11))
    print("Min Delete Operations Example:", SolutionMinDeleteOperations().minDistance("sea", "eat"))
