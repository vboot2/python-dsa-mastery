"""
Day 45: Dynamic Programming (1D, 2D, LCS)
"""

# ----------------------------------------
# Example 1: Minimum Edit Distance
# ----------------------------------------
def example_one():
    word1, word2 = "horse", "ros"
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

print("Output Example 1 (Edit Distance):", example_one())


# ----------------------------------------
# Example 2: Coin Change Problem
# ----------------------------------------
def example_two():
    coins = [1, 2, 5]
    amount = 11
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print("Output Example 2 (Coin Change):", example_two())
