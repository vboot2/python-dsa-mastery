"""
Day 18: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Letter Combinations of a Phone Number (LeetCode 17, Medium)
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# ---------------------------------------------------------
class SolutionLetterCombinations:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return
            for ch in phone_map[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# ---------------------------------------------------------
# Problem 2: N-Queens (LeetCode 51, Hard)
# Link: https://leetcode.com/problems/n-queens/
# ---------------------------------------------------------
class SolutionNQueens:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r-c) in diag1 or (r+c) in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        backtrack(0)
        return res


# ---------------------------------------------------------
# Problem 3: Sudoku Solver (LeetCode 37, Hard)
# Link: https://leetcode.com/problems/sudoku-solver/
# ---------------------------------------------------------
class SolutionSudokuSolver:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(r, c, ch):
            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch:
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3] == ch:
                    return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1, 10)):
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        backtrack()


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Letter Combinations:", SolutionLetterCombinations().letterCombinations("23"))
    print("N-Queens n=4:", SolutionNQueens().solveNQueens(4))

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    SolutionSudokuSolver().solveSudoku(board)
    print("Sudoku Solved Board:")
    for row in board:
        print(row)
