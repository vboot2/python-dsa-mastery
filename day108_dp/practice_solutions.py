"""
Day 108: DP - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Pascal's Triangle (LeetCode 118, Easy)
# Link: https://leetcode.com/problems/pascals-triangle/
# ---------------------------------------------------------
class SolutionProblemOne:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        DP construction:
        Each row is built from the previous row.
        """
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle


# ---------------------------------------------------------
# Problem: Pascal's Triangle II (LeetCode 119, Easy)
# Link: https://leetcode.com/problems/pascals-triangle-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Space-optimized DP:
        Build row in-place from right to left.
        """
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row


# ---------------------------------------------------------
# Problem: Is Subsequence (LeetCode 392, Easy)
# Link: https://leetcode.com/problems/is-subsequence/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Greedy / DP intuition:
        Match characters in order using two pointers.
        """
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


# ---------------------------------------------------------
# Problem: Fibonacci Number (LeetCode 509, Easy)
# Link: https://leetcode.com/problems/fibonacci-number/
# ---------------------------------------------------------
class SolutionProblemFour:
    def fib(self, n: int) -> int:
        """
        DP with constant space.
        """
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().generate(5))
    print("Problem Two Example:", SolutionProblemTwo().getRow(4))
    print("Problem Three Example:", SolutionProblemThree().isSubsequence("abc", "ahbgdc"))
    print("Problem Four Example:", SolutionProblemFour().fib(10))
