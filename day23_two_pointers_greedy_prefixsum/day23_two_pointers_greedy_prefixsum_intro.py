"""
Day 23: Two Pointers, Greedy, Prefix Sum

These are common techniques to optimize array-based problems:
- Two Pointers: Efficiently traverse arrays from both ends.
- Greedy: Make locally optimal choices leading to global optimum.
- Prefix Sum: Precompute cumulative sums for fast range queries.
"""

# Example 1: Two Pointers (pair with target sum)
def example_one():
    nums = [1, 2, 3, 4, 6]
    target = 6
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

print("Output Example 1:", example_one())


# Example 2: Prefix Sum (range sum queries)
def example_two():
    nums = [2, 4, 6, 8, 10]
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n)
    # sum of subarray nums[1:4] → 4 + 6 + 8 = 18
    return prefix[4] - prefix[1]

print("Output Example 2:", example_two())
