"""
Day 77: DP String / Subarray
"""

# Example 1: Regex DP (similar to LeetCode 10)
def example_one():
    """
    Implement pattern matching where:
      '.'  → matches any character
      '*'  → matches zero or more of the previous character
    """

    s = "aab"
    p = "c*a*b"

    # DP table creation
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, len(p) + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    # Fill DP
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                # zero or more occurrences
                dp[i][j] = dp[i][j - 2] or \
                    ((p[j - 2] == "." or p[j - 2] == s[i - 1]) and dp[i - 1][j])

    return dp[-1][-1]

print("Output Example 1:", example_one())


# Example 2: Wildcard DP (similar to LeetCode 44)
def example_two():
    """
    Pattern rules:
      '?'  → matches any single char
      '*'  → matches any sequence
    """

    s = "adceb"
    p = "*a*b"

    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(1, len(p) + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):

            if p[j - 1] == "*" :
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[-1][-1]

print("Output Example 2:", example_two())
