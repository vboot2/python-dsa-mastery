"""
Day 49: Dynamic Programming (Sequences & Path Minimization)

DP patterns covered:
- Largest Divisible Subset → subset DP with parent reconstruction
- Wiggle Subsequence → state DP (up/down)
- Minimum Falling Path Sum → in-place bottom-up grid DP
"""

# -------------------------------
# Example 1: Largest Divisible Subset
# -------------------------------
def largest_divisible_subset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n          # dp[i] = length of largest subset ending at i
    parent = [-1] * n     # parent pointer to reconstruct subset
    max_len, max_idx = 1, 0

    for i in range(n):
        for j in range(i):
            # if nums[i] divisible by nums[j], we can extend subset at j
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len, max_idx = dp[i], i

    # reconstruct subset
    res = []
    while max_idx != -1:
        res.append(nums[max_idx])
        max_idx = parent[max_idx]
    return res[::-1]

print("Largest Divisible Subset for [1,2,4,8]:", largest_divisible_subset([1,2,4,8]))


# -------------------------------
# Example 2: Wiggle Subsequence
# -------------------------------
def wiggle_max_length(nums):
    if not nums:
        return 0
    # up = length of wiggle subseq ending with an up move
    # down = length ending with a down move
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
    return max(up, down)

print("Wiggle Subsequence Length for [1,7,4,9,2,5]:", wiggle_max_length([1,7,4,9,2,5]))


# -------------------------------
# Example 3: Minimum Falling Path Sum
# -------------------------------
def min_falling_path_sum(matrix):
    # modifies matrix in-place bottom-up to store best sums
    if not matrix:
        return 0
    n = len(matrix)
    # start from second last row and propagate best choices upward
    for i in range(n-2, -1, -1):
        for j in range(n):
            best = matrix[i+1][j]  # directly below
            if j > 0:
                best = min(best, matrix[i+1][j-1])
            if j < n-1:
                best = min(best, matrix[i+1][j+1])
            matrix[i][j] += best
    # minimal falling path sum is min element in top row after update
    return min(matrix[0])

print("Minimum Falling Path Sum for [[2,1,3],[6,5,4],[7,8,9]]:", 
      min_falling_path_sum([[2,1,3],[6,5,4],[7,8,9]]))
