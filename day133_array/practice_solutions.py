"""Day 133: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Find N Unique Integers Sum up to Zero (LeetCode 1304)
# Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# ---------------------------------------------------------
class SolutionProblemOne:
    def sumZero(self, n: int) -> List[int]:
        result = []
        x = 1
        while len(result) < n:
            if len(result) + 2 <= n:
                result.extend([x, -x])
                x += 1
            else:
                result.append(0)
        return result


# ---------------------------------------------------------
# Problem: Decompress Run-Length Encoded List (LeetCode 1313)
# Link: https://leetcode.com/problems/decompress-run-length-encoded-list/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])
        return result


# ---------------------------------------------------------
# Problem: The K Weakest Rows in a Matrix (LeetCode 1337)
# Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# ---------------------------------------------------------
class SolutionProblemThree:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = [(sum(row), i) for i, row in enumerate(mat)]
        strength.sort()
        return [idx for _, idx in strength[:k]]


# ---------------------------------------------------------
# Problem: Count Negative Numbers in a Sorted Matrix (LeetCode 1351)
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# ---------------------------------------------------------
class SolutionProblemFour:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = 0, cols - 1
        count = 0

        while r < rows and c >= 0:
            if grid[r][c] < 0:
                count += rows - r
                c -= 1
            else:
                r += 1
        return count


# ---------------------------------------------------------
# Problem: Sort Integers by The Number of 1 Bits (LeetCode 1356)
# Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# ---------------------------------------------------------
class SolutionProblemFive:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


# ---------------------------------------------------------
# Problem: Lucky Numbers in a Matrix (LeetCode 1380)
# Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# ---------------------------------------------------------
class SolutionProblemSix:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = {min(row) for row in matrix}
        max_cols = {max(col) for col in zip(*matrix)}
        return list(min_rows & max_cols)


# ---------------------------------------------------------
# Problem: Spiral Matrix II (LeetCode 59, Medium)
# Link: https://leetcode.com/problems/spiral-matrix-ii/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left = top = 0
        right = bottom = n - 1
        num = 1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                matrix[top][c] = num
                num += 1
            top += 1

            for r in range(top, bottom + 1):
                matrix[r][right] = num
                num += 1
            right -= 1

            for c in range(right, left - 1, -1):
                matrix[bottom][c] = num
                num += 1
            bottom -= 1

            for r in range(bottom, top - 1, -1):
                matrix[r][left] = num
                num += 1
            left += 1

        return matrix


# ---------------------------------------------------------
# Problem: Set Matrix Zeroes (LeetCode 73, Medium)
# Link: https://leetcode.com/problems/set-matrix-zeroes/
# ---------------------------------------------------------
class SolutionProblemEight:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0


# ---------------------------------------------------------
# Problem: Remove Duplicates from Sorted Array II (LeetCode 80, Medium)
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# ---------------------------------------------------------
class SolutionProblemNine:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i


# ---------------------------------------------------------
# Problem: Search in Rotated Sorted Array II (LeetCode 81, Medium)
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# ---------------------------------------------------------
class SolutionProblemTen:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("1304 Example:", SolutionProblemOne().sumZero(5))
    print(
        "1337 Example:",
        SolutionProblemThree().kWeakestRows([[1, 1, 0], [1, 1, 1], [1, 0, 0]], 2),
    )
    print(
        "80 Example:",
        SolutionProblemNine().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]),
    )
