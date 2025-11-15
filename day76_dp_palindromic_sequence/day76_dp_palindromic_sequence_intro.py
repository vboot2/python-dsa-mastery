"""
Day 76: DP Palindromic / Sequence
Palindrome partitioning,
minimum cuts, and sequence transformations.
"""

# -----------------------------------------------------
# Example 1: Min cuts for palindrome partitioning (DP)
# -----------------------------------------------------

def example_one(s: str) -> int:
    """
    Classic DP:
    - Precompute palindrome table using expand or DP
    - dp[i] = minimum cuts needed for s[:i+1]
    """
    n = len(s)
    pal = [[False]*n for _ in range(n)]

    # Fill pal[i][j] = True if s[i:j+1] is palindrome
    for r in range(n):
        for l in range(r+1):
            if s[l] == s[r] and (r-l < 2 or pal[l+1][r-1]):
                pal[l][r] = True

    dp = [float('inf')] * n

    for i in range(n):
        if pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if pal[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

print("Output Example 1:", example_one("aab"))  # Expected: 1


# -----------------------------------------------------
# Example 2: Longest Palindromic Subsequence (LPS)
# -----------------------------------------------------

def example_two(s: str) -> int:
    """
    DP on subsequences:
    - dp[l][r] = LPS inside s[l:r+1]
    """
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

print("Output Example 2:", example_two("bbbab"))  # Expected: 4
