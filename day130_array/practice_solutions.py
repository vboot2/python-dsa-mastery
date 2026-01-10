"""Day 130: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Projection Area of 3D Shapes (LeetCode 883, Easy)
# Link: https://leetcode.com/problems/projection-area-of-3d-shapes/
# ---------------------------------------------------------
class SolutionProblemOne:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(v > 0 for row in grid for v in row)
        front = sum(max(row) for row in grid)
        side = sum(max(col) for col in zip(*grid))
        return top + front + side


# ---------------------------------------------------------
# Problem: Surface Area of 3D Shapes (LeetCode 892, Easy)
# Link: https://leetcode.com/problems/surface-area-of-3d-shapes/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    area += 2
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + di, j + dj
                        neighbor = grid[ni][nj] if 0 <= ni < n and 0 <= nj < n else 0
                        area += max(grid[i][j] - neighbor, 0)

        return area


# ---------------------------------------------------------
# Problem: Monotonic Array (LeetCode 896, Easy)
# Link: https://leetcode.com/problems/monotonic-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                inc = False
            if nums[i] > nums[i - 1]:
                dec = False
        return inc or dec


# ---------------------------------------------------------
# Problem: Smallest Range I (LeetCode 908, Easy)
# Link: https://leetcode.com/problems/smallest-range-i/
# ---------------------------------------------------------
class SolutionProblemFour:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)


# ---------------------------------------------------------
# Problem: Valid Mountain Array (LeetCode 941, Easy)
# Link: https://leetcode.com/problems/valid-mountain-array/
# ---------------------------------------------------------
class SolutionProblemFive:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


# ---------------------------------------------------------
# Problem: Delete Columns to Make Sorted (LeetCode 944, Easy)
# Link: https://leetcode.com/problems/delete-columns-to-make-sorted/
# ---------------------------------------------------------
class SolutionProblemSix:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        return count


# ---------------------------------------------------------
# Problem: Largest Perimeter Triangle (LeetCode 976, Easy)
# Link: https://leetcode.com/problems/largest-perimeter-triangle/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


# ---------------------------------------------------------
# Problem: Add to Array-Form of Integer (LeetCode 989, Easy)
# Link: https://leetcode.com/problems/add-to-array-form-of-integer/
# ---------------------------------------------------------
class SolutionProblemEight:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                k //= 10
                i -= 1
            else:
                num.insert(0, k % 10)
                k //= 10
        return num


# ---------------------------------------------------------
# Problem: Available Captures for Rook (LeetCode 999, Easy)
# Link: https://leetcode.com/problems/available-captures-for-rook/
# ---------------------------------------------------------
class SolutionProblemNine:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    r, c = i, j

        captures = 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i, j = r, c
            while 0 <= i < 8 and 0 <= j < 8:
                i += dr
                j += dc
                if not (0 <= i < 8 and 0 <= j < 8):
                    break
                if board[i][j] == "B":
                    break
                if board[i][j] == "p":
                    captures += 1
                    break
        return captures


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("896 Example:", SolutionProblemThree().isMonotonic([1, 2, 2, 3]))
    print("941 Example:", SolutionProblemFive().validMountainArray([0, 3, 2, 1]))
    print("989 Example:", SolutionProblemEight().addToArrayForm([2, 7, 4], 181))
