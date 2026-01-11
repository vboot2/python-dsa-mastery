"""Day 131: Array
Greedy decisions, prefix evaluation,
sorting-based optimizations, and geometric checks.
"""


# Example 1: Maximize array sum after k negations
def example_one():
    """
    Greedy approach:
    - Sort array
    - Flip negative numbers first
    - If k remains odd, flip smallest absolute value
    """
    nums = [-2, 9, 3, -1]
    k = 2

    nums.sort()
    i = 0

    while i < len(nums) and k > 0 and nums[i] < 0:
        nums[i] = -nums[i]
        i += 1
        k -= 1

    if k % 2 == 1:
        nums[nums.index(min(nums))] *= -1

    return sum(nums)


print("Output Example 1:", example_one())


# Example 2: Check if array can be split into equal sum parts
def example_two():
    """
    Prefix sum scan:
    - Find prefix with sum == total/3
    - Find another prefix with same sum
    """
    arr = [0, 2, 1, -1, 1, -1, 1]
    total = sum(arr)

    if total % 3 != 0:
        return False

    target = total // 3
    prefix = count = 0

    for num in arr:
        prefix += num
        if prefix == target:
            count += 1
            prefix = 0

    return count >= 3


print("Output Example 2:", example_two())
