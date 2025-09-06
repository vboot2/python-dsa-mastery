"""
Day 06: Prefix Sum

Prefix Sum is a technique where we precompute cumulative sums
so we can query ranges efficiently.
"""

# Example 1: Range sum queries
nums = [1, 2, 3, 4, 5]
prefix = [0] * (len(nums) + 1)

for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

# Range sum of [1, 3] → 2 + 3 + 4
l, r = 1, 3
print("Range sum [1,3]:", prefix[r+1] - prefix[l])

# Example 2: Subarray sum equals k (basic)
nums = [1, 2, 3, -2, 5]
k = 3
count = 0
prefix_sum = 0
seen = {0: 1}  # prefix sum → frequency

for num in nums:
    prefix_sum += num
    if prefix_sum - k in seen:
        count += seen[prefix_sum - k]
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

print("Subarrays with sum =", k, ":", count)
