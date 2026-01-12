"""Day 132: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Minimum Cost to Move Chips to The Same Position (LeetCode 1217)
# Link: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# ---------------------------------------------------------
class SolutionProblemOne:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = odd = 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


# ---------------------------------------------------------
# Problem: Check If It Is a Straight Line (LeetCode 1232)
# Link: https://leetcode.com/problems/check-if-it-is-a-straight-line/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for x, y in coordinates[2:]:
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True


# ---------------------------------------------------------
# Problem: Cells with Odd Values in a Matrix (LeetCode 1252)
# Link: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# ---------------------------------------------------------
class SolutionProblemThree:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    count += 1
        return count


# ---------------------------------------------------------
# Problem: Shift 2D Grid (LeetCode 1260)
# Link: https://leetcode.com/problems/shift-2d-grid/
# ---------------------------------------------------------
class SolutionProblemFour:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        flat = [num for row in grid for num in row]

        k %= len(flat)
        flat = flat[-k:] + flat[:-k]

        return [flat[i * cols : (i + 1) * cols] for i in range(rows)]


# ---------------------------------------------------------
# Problem: Minimum Time Visiting All Points (LeetCode 1266)
# Link: https://leetcode.com/problems/minimum-time-visiting-all-points/
# ---------------------------------------------------------
class SolutionProblemFive:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            time += max(abs(x2 - x1), abs(y2 - y1))
        return time


# ---------------------------------------------------------
# Problem: Element Appearing More Than 25% In Sorted Array (LeetCode 1287)
# Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findSpecialInteger(self, arr: List[int]):
        step = len(arr) // 4

        for x in range(len(arr)):
            if arr[x] == arr[x + step]:
                return arr[x]


# ---------------------------------------------------------
# Problem: Find Numbers with Even Number of Digits (LeetCode 1295)
# Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(num)) % 2 == 0 for num in nums)


# ---------------------------------------------------------
# Problem: Replace Elements with Greatest Element on Right Side (LeetCode 1299)
# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# ---------------------------------------------------------
class SolutionProblemEight:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(max_right, temp)
        return arr


# ---------------------------------------------------------
# Problem: Next Permutation (LeetCode 31, Medium)
# Link: https://leetcode.com/problems/next-permutation/
# ---------------------------------------------------------
class SolutionProblemNine:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1 :] = reversed(nums[i + 1 :])


# ---------------------------------------------------------
# Problem: Valid Sudoku (LeetCode 36, Medium)
# Link: https://leetcode.com/problems/valid-sudoku/
# ---------------------------------------------------------
class SolutionProblemTen:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                b = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        return True


# ---------------------------------------------------------
# Problem: Rotate Image (LeetCode 48, Medium)
# Link: https://leetcode.com/problems/rotate-image/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("1217 Example:", SolutionProblemOne().minCostToMoveChips([1, 2, 3]))
    print("1299 Example:", SolutionProblemEight().replaceElements([17, 18, 5, 4, 6, 1]))
