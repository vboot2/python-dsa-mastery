"""
Day 44: Dynamic Programming (1D, 2D, LCS)

Dynamic Programming can be applied in optimization and sequence analysis problems.
"""

# -------------------------------
# Example 1: Maximum Subarray Sum (Kadane’s Algorithm)
# -------------------------------
def example_one():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    current_sum = max_sum = nums[0]
    for n in nums[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum

print("Output Example 1 (Max Subarray Sum):", example_one())


# -------------------------------
# Example 2: Longest Increasing Subsequence (LIS)
# -------------------------------
def example_two():
    nums = [10,9,2,5,3,7,101,18]
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print("Output Example 2 (Longest Increasing Subsequence):", example_two())
