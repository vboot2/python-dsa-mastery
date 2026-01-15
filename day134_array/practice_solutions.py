"""Day 134: Array - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Find the Distance Value Between Two Arrays (LeetCode 1385)
# ---------------------------------------------------------
class SolutionProblemOne:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                count += 1
        return count


# ---------------------------------------------------------
# Problem: Create Target Array in the Given Order (LeetCode 1389)
# ---------------------------------------------------------
class SolutionProblemTwo:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target


# ---------------------------------------------------------
# Problem: Surrounded Regions (LeetCode 130, Medium)
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


# ---------------------------------------------------------
# Problem: Evaluate Reverse Polish Notation (LeetCode 150, Medium)
# ---------------------------------------------------------
class SolutionProblemFour:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[0]


# ---------------------------------------------------------
# Problem: Rotate Array (LeetCode 189, Medium)
# ---------------------------------------------------------
class SolutionProblemFive:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "1385 Example:",
        SolutionProblemOne().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2),
    )
    print(
        "1389 Example:",
        SolutionProblemTwo().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]),
    )
    print("150 Example:", SolutionProblemFour().evalRPN(["2", "1", "+", "3", "*"]))
