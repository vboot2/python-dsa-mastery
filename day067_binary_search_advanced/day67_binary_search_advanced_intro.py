"""
Day 67: Binary Search (Advanced)
"""


# -------------------------------
# Example 1: Classic binary search with condition checks
# -------------------------------
def example_one(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print("Output Example 1 (target=6):", example_one([1, 3, 5, 6, 8, 9], 6))


# -------------------------------
# Example 2: Search in a 2D matrix using binary flattening
# -------------------------------
def example_two(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = (low + high) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


print(
    "Output Example 2 (matrix search):",
    example_two([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9),
)


# -------------------------------
# Example 3: Binary search on partition (Median of Two Sorted Arrays)
# -------------------------------
def example_three(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
        minX = float("inf") if partitionX == x else nums1[partitionX]
        maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
        minY = float("inf") if partitionY == y else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1


print("Output Example 3 (median of [1,3] and [2]):", example_three([1, 3], [2]))
