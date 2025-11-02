"""
Day 63: Dynamic Programming (LCS, Subsets, Knapsack)
"""


# Example 1: Subset Sum Decision (1D DP)
def example_one():
    nums = [1, 5, 11, 5]
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


print("Output Example 1:", example_one())


# Example 2: Longest Common Subsequence (2D DP)
def example_two():
    text1, text2 = "abcde", "ace"
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


print("Output Example 2:", example_two())
