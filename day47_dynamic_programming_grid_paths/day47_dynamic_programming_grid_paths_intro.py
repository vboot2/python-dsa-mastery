"""
Day 47: Dynamic Programming (Grid Paths - 2D DP)

Grid-based DP problems that deal with movement, cost minimization, and path matching.

- Unique Paths → Counting paths using DP grid
- Minimum Path Sum → Minimizing path sum in a grid
- Interleaving String → DP string combination problem
"""

# -------------------------------
# Example 1: Unique Paths
# -------------------------------
def unique_paths(m: int, n: int) -> int:
    # Each cell stores number of ways to reach it
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

print("Unique Paths in 3x7 grid:", unique_paths(3, 7))


# -------------------------------
# Example 2: Minimum Path Sum
# -------------------------------
def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # Fill first row and column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill rest of grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]

print("Minimum Path Sum for [[1,3,1],[1,5,1],[4,2,1]]:", min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))


# -------------------------------
# Example 3: Interleaving String
# -------------------------------
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True

    for i in range(1, len(s1)+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

    for j in range(1, len(s2)+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

    return dp[-1][-1]

print("Is 'aadbbcbcac' interleaving of 'aabcc' and 'dbbca'? ->", is_interleave("aabcc", "dbbca", "aadbbcbcac"))
