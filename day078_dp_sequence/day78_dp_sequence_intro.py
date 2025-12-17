"""
Day 78: DP Sequence
DP Sequence problems involve building optimal subsequences or counting subsequences using dynamic programming.
These typically include variations like LIS counts, arithmetic subsequences, and nested envelope problems.
"""

# ------------------------------------------------------
# Example 1: Longest Increasing Subsequence Count (mini-version)
# ------------------------------------------------------

def example_one(nums):
    """
    Compute the number of LIS (Longest Increasing Subsequences).
    """
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n      # length of LIS ending at i
    count = [1] * n   # number of LIS ending at i

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]

    max_len = max(dp)
    return sum(c for l, c in zip(dp, count) if l == max_len)


print("Output Example 1:", example_one([1,3,5,4,7]))  # Expected: 2


# ------------------------------------------------------
# Example 2: Number of Arithmetic Slices (mini-version)
# ------------------------------------------------------

def example_two(nums):
    """
    Count arithmetic subarrays of length >= 3.
    """
    if len(nums) < 3:
        return 0

    total = 0
    curr = 0  # number of arithmetic subarrays ending at current index

    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            curr += 1
            total += curr
        else:
            curr = 0

    return total


print("Output Example 2:", example_two([1,2,3,4]))  # Expected: 3
