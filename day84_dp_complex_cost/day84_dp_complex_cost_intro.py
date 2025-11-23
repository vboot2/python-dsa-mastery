"""
Day 84: DP – Complex Cost
DP problems where transitions involve non-trivial cost functions,
such as cross-sequence matching, weighted substructure scoring, and interval DP.
"""

# ---------------------------------------------------
# Example 1: Cross-sequence DP (Longest Common Subsequence variant)
# ---------------------------------------------------
def example_one():
    A = [1, 4, 2]
    B = [1, 2, 4]

    m, n = len(A), len(B)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # LCS-style DP to show cross-sequence matching
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[m][n]

print("Output Example 1:", example_one())


# ---------------------------------------------------
# Example 2: Interval DP – Cutting a board with costs
# ---------------------------------------------------
def example_two():
    cuts = [1, 3, 4]
    n = 7
    arr = [0] + cuts + [n]
    arr.sort()
    m = len(arr)

    from functools import lru_cache

    @lru_cache(None)
    def dp(i, j):
        if j - i <= 1:
            return 0
        best = float('inf')
        for k in range(i+1, j):
            best = min(best, dp(i, k) + dp(k, j) + arr[j] - arr[i])
        return best

    return dp(0, m-1)

print("Output Example 2:", example_two())
