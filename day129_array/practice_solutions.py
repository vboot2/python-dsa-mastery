"""Day 129: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Number of Lines To Write String (LeetCode 806)
# Link: https://leetcode.com/problems/number-of-lines-to-write-string/
# ---------------------------------------------------------
class SolutionProblemOne:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current = 0

        for ch in s:
            w = widths[ord(ch) - ord("a")]
            if current + w > 100:
                lines += 1
                current = w
            else:
                current += w

        return [lines, current]


# ---------------------------------------------------------
# Problem: Largest Triangle Area (LeetCode 812)
# Link: https://leetcode.com/problems/largest-triangle-area/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return (
                abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
                / 2
            )

        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, area(points[i], points[j], points[k]))

        return max_area


# ---------------------------------------------------------
# Problem: Flipping an Image (LeetCode 832)
# Link: https://leetcode.com/problems/flipping-an-image/
# ---------------------------------------------------------
class SolutionProblemThree:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image


# ---------------------------------------------------------
# Problem: Lemonade Change (LeetCode 860)
# Link: https://leetcode.com/problems/lemonade-change/
# ---------------------------------------------------------
class SolutionProblemFour:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


# ---------------------------------------------------------
# Problem: Transpose Matrix (LeetCode 867)
# Link: https://leetcode.com/problems/transpose-matrix/
# ---------------------------------------------------------
class SolutionProblemFive:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]

        return result


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "806 Example:",
        SolutionProblemOne().numberOfLines([10] * 26, "abcdefghijklmnopqrstuvwxyz"),
    )
    print(
        "812 Example:",
        SolutionProblemTwo().largestTriangleArea(
            [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
        ),
    )
    print(
        "832 Example:",
        SolutionProblemThree().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]),
    )
    print("860 Example:", SolutionProblemFour().lemonadeChange([5, 5, 5, 10, 20]))
    print("867 Example:", SolutionProblemFive().transpose([[1, 2, 3], [4, 5, 6]]))
