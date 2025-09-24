"""
Day 24: Two Pointers, Greedy, Prefix Sum

- Two Pointers: Efficient traversal from both ends
- Greedy: Locally optimal choices leading to global solution
- Prefix Sum: Precompute cumulative sums for quick range queries
"""

# Example 1: Two Pointers (Trapping Rain Water - simplified demo)
def example_one():
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water

print("Output Example 1 (Water trapped):", example_one())


# Example 2: Greedy (Gas Station feasibility check)
def example_two():
    gas, cost = [1,2,3,4,5], [3,4,5,1,2]
    if sum(gas) < sum(cost):
        return -1
    total, start = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start

print("Output Example 2 (Starting station):", example_two())


# Example 3: Prefix Sum (Subarray sums quickly)
def example_three():
    nums = [1,2,3,4,5]
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    # sum of nums[1:4] = 2+3+4
    return prefix[4] - prefix[1]

print("Output Example 3 (Prefix sum range 1-3):", example_three())
