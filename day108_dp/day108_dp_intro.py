"""
Day 108: Dynamic Programming (DP)
DP solves problems by breaking them into overlapping subproblems and storing results
to avoid repeated computation.
"""

# Example 1: Fibonacci using bottom-up DP
def example_one():
    """
    Bottom-up DP:
    dp[i] = dp[i-1] + dp[i-2]
    """
    n = 10
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print("Output Example 1:", example_one())


# Example 2: DP for subsequence checking
def example_two():
    """
    Check if one string is a subsequence of another
    using two pointers (DP intuition: ordered matching).
    """
    s = "abc"
    t = "ahbgdc"

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

print("Output Example 2:", example_two())
