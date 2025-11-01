"""
Day 62: 1D / 2D Dynamic Programming
"""


# Example 1: 1D DP - Fibonacci Numbers
def example_one():
    n = 10
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print("Output Example 1:", example_one())


# Example 2: 2D DP - Minimum Path Sum in a Grid
def example_two():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # First row and column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill rest of table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


print("Output Example 2:", example_two())
