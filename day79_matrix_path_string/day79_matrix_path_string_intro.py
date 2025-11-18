"""
Day 79: Matrix/Path + String DP
Matrix Path DP solves optimal routes in grids (min/max cost).
String DP solves pairwise operations such as edit distance or deletion cost.
"""

# ---------------------------------------------------------
# Example 1: Matrix Path DP (Min Path Sum Variant)
# ---------------------------------------------------------

def example_one(grid):
    """
    Classic matrix DP example:
    Find min path sum from top-left to bottom-right
    moving only down or right.
    """
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

print("Output Example 1:", example_one([[1,3,1],[1,5,1],[4,2,1]]))


# ---------------------------------------------------------
# Example 2: String DP – Minimum Deletion Cost to Match Strings
# ---------------------------------------------------------

def example_two(s1, s2):
    """
    Demonstrates the DP pattern used in LC 712:
    Minimum ASCII Delete Sum for Two Strings.
    """

    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # delete all from s1
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])

    # delete all from s2
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + ord(s1[i-1]),   # delete from s1
                    dp[i][j-1] + ord(s2[j-1])    # delete from s2
                )

    return dp[m][n]

print("Output Example 2:", example_two("sea", "eat"))
