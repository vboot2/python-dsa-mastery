"""
Day 109: Dynamic Programming (DP)
DP uses optimal substructure and overlapping subproblems to build solutions
incrementally instead of recomputing results.
"""

# Example 1: Tribonacci (bottom-up DP)
def example_one():
    """
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    """
    n = 6
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

print("Output Example 1:", example_one())


# Example 2: DP for string repetition detection
def example_two():
    """
    DP intuition for string matching:
    Track the longest prefix of target matched so far.
    """
    sequence = ["a", "b", "c"]
    word = "abc"
    count = 0
    curr = ""

    for s in sequence:
        curr += s
        if curr.endswith(word):
            count += 1
            curr = ""

    return count

print("Output Example 2:", example_two())
