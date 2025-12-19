"""
Day 110: Dynamic Programming (DP)
DP solves problems by breaking them into overlapping subproblems and
building optimal solutions using previously computed results.
"""

# Example 1: Maximum Subarray (Kadane’s Algorithm)
def example_one():
    """
    dp[i] = max subarray sum ending at index i
    Optimized to O(1) space using running variables.
    """
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    curr_sum = max_sum = nums[0]

    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print("Output Example 1:", example_one())


# Example 2: Perfect Squares (DP bottom-up)
def example_two():
    """
    dp[i] = minimum number of perfect squares that sum to i
    """
    n = 12
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

print("Output Example 2:", example_two())
