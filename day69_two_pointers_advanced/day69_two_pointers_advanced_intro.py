"""
Day 69: Two Pointers (Advanced)

1. Traversing multi-dimensional structures (Matrix Diagonal Order)
2. Sorting in-place using pointer swaps (Dutch National Flag)
3. Cycle detection (Floyd's Tortoise and Hare)
"""


# -------------------------------------------------------
# Example 1: Diagonal Traverse (Matrix Traversal)
# -------------------------------------------------------
def example_one(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    res = []
    r, c = 0, 0
    direction = 1  # 1 for up-right, -1 for down-left

    for _ in range(rows * cols):
        res.append(matrix[r][c])
        if direction == 1:
            if c == cols - 1:
                r += 1
                direction = -1
            elif r == 0:
                c += 1
                direction = -1
            else:
                r -= 1
                c += 1
        else:
            if r == rows - 1:
                c += 1
                direction = 1
            elif c == 0:
                r += 1
                direction = 1
            else:
                r += 1
                c -= 1
    return res


print("Example 1 (Diagonal Traverse):", example_one([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# -------------------------------------------------------
# Example 2: Sort Colors (Dutch National Flag)
# -------------------------------------------------------
def example_two(nums: list[int]) -> list[int]:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


print("Example 2 (Sort Colors):", example_two([2, 0, 2, 1, 1, 0]))


# -------------------------------------------------------
# Example 3: Find Duplicate Number (Cycle Detection)
# -------------------------------------------------------
def example_three(nums: list[int]) -> int:
    # Floyd’s Tortoise and Hare algorithm
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find cycle entrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


print("Example 3 (Find Duplicate Number):", example_three([1, 3, 4, 2, 2]))
