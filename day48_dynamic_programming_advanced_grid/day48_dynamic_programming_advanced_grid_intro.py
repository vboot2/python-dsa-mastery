"""
Day 48: Dynamic Programming (1D, 2D, LCS)

2D Dynamic Programming patterns:
- Grid traversal with obstacles
- Minimum path sums
- Largest square submatrices
"""

# ---------------------------------------------------------
# Example 1: Unique Paths II (Grid DP with Obstacles)
# ---------------------------------------------------------
def unique_paths_with_obstacles(grid):
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0

    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0

    # Fill the grid
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


print("Unique Paths II:", unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))


# ---------------------------------------------------------
# Example 2: Triangle Minimum Path Sum (Bottom-Up DP)
# ---------------------------------------------------------
def minimum_total(triangle):
    dp = triangle[-1][:]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    return dp[0]


print("Triangle Minimum Total:", minimum_total([[2],[3,4],[6,5,7],[4,1,8,3]]))


# ---------------------------------------------------------
# Example 3: Maximal Square (2D DP for submatrix)
# ---------------------------------------------------------
def maximal_square(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_side = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side


print("Maximal Square Area:", maximal_square([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))
