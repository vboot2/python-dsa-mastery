"""
Day 22: Two Pointers, Greedy, Prefix Sum

Today's problems combine techniques:
1. Two Pointers - Finding pairs/triplets that satisfy conditions.
2. Greedy - Making optimal local choices.
3. Prefix Sum - Efficiently computing ranges.
"""

# Example 1: Two pointers inward for max water container
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        # Move the pointer at the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print("Output Example 1:", max_area([1,8,6,2,5,4,8,3,7]))


# Example 2: Finding triplets that sum to zero
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return result

print("Output Example 2:", three_sum([-1,0,1,2,-1,-4]))


# Example 3: Closest 3-sum value
def three_sum_closest(nums, target):
    nums.sort()
    closest = float("inf")
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if abs(target - total) < abs(target - closest):
                closest = total
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return target
    return closest

print("Output Example 3:", three_sum_closest([-1,2,1,-4], 1))
