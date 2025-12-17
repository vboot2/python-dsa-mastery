"""
Day 67: Binary Search (Advanced) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Median of Two Sorted Arrays (LeetCode 4, Hard)
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# ---------------------------------------------------------


class SolutionMedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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


# ---------------------------------------------------------
# Problem 2: Search a 2D Matrix (LeetCode 74, Medium)
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# ---------------------------------------------------------


class SolutionSearch2DMatrix:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
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


# ---------------------------------------------------------
# Problem 3: Search a 2D Matrix II (LeetCode 240, Medium)
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# ---------------------------------------------------------


class SolutionSearch2DMatrixII:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Median of [1,3] and [2]:",
        SolutionMedianOfTwoSortedArrays().findMedianSortedArrays([1, 3], [2]),
    )
    print(
        "Search 2D Matrix (74):",
        SolutionSearch2DMatrix().searchMatrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9),
    )
    print(
        "Search 2D Matrix II (240):",
        SolutionSearch2DMatrixII().searchMatrix(
            [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 5
        ),
    )
