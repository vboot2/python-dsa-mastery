"""
Day 69: Two Pointers (Advanced) - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem 1: Diagonal Traverse (LeetCode 498, Medium)
# Link: https://leetcode.com/problems/diagonal-traverse/
# ---------------------------------------------------------
class SolutionDiagonalTraverse:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat:
            return []
        rows, cols = len(mat), len(mat[0])
        res = []
        r, c = 0, 0
        direction = 1

        for _ in range(rows * cols):
            res.append(mat[r][c])
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


# ---------------------------------------------------------
# Problem 2: Sort Colors (LeetCode 75, Medium)
# Link: https://leetcode.com/problems/sort-colors/
# ---------------------------------------------------------
class SolutionSortColors:
    def sortColors(self, nums: list[int]) -> None:
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


# ---------------------------------------------------------
# Problem 3: Find the Duplicate Number (LeetCode 287, Medium)
# Link: https://leetcode.com/problems/find-the-duplicate-number/
# ---------------------------------------------------------
class SolutionFindDuplicate:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Diagonal Traverse:",
        SolutionDiagonalTraverse().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    )
    print("Sort Colors:", SolutionSortColors().sortColors([2, 0, 2, 1, 1, 0]))
    print(
        "Find Duplicate Number:", SolutionFindDuplicate().findDuplicate([1, 3, 4, 2, 2])
    )
