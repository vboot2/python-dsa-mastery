"""
Day 82: DP - Sequence/Matrix
DP that operates over 2D grids and sequences:
- Count submatrices (matrix DP)
- Scramble-string equivalence (interval DP)
- Matrix-chain style interval DP (burst balloons)
"""

# Example 1: Simple matrix DP – counting 1-squares
def example_one():
    # Count number of square submatrices of all 1s (small example)
    mat = [
        [1,1],
        [1,1]
    ]
    n,m = len(mat), len(mat[0])
    dp = [[0]*m for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # expand square
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                total += dp[i][j]

    return total

print("Output Example 1:", example_one())


# Example 2: Interval DP – burst balloons structure
def example_two():
    nums = [3,1,5]
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    # length
    for length in range(2, n):
        for l in range(0, n-length):
            r = l + length
            for k in range(l+1, r):  # last balloon popped
                dp[l][r] = max(dp[l][r],
                                nums[l]*nums[k]*nums[r] + dp[l][k] + dp[k][r])
    return dp[0][-1]

print("Output Example 2:", example_two())
