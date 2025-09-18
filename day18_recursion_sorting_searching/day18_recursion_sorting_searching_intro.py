"""
Day 18: Recursion, Sorting, Searching

Focus: Backtracking with recursion on combinatorial problems.
"""

# -------------------------------
# Example 1: Letter combinations of a phone number
# -------------------------------
def letter_combinations(digits: str) -> list[str]:
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

print("Letter Combinations for '23':", letter_combinations("23"))


# -------------------------------
# Example 2: N-Queens (placing queens safely)
# -------------------------------
def solve_n_queens(n: int) -> list[list[str]]:
    board = [["."] * n for _ in range(n)]
    res = []

    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c

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

print("N-Queens solutions for n=4:", solve_n_queens(4))


# -------------------------------
# Example 3: Sudoku validation (helper demo)
# -------------------------------
def is_valid(board, r, c, ch):
    for i in range(9):
        if board[r][i] == ch or board[i][c] == ch:
            return False
        if board[3*(r//3) + i//3][3*(c//3) + i%3] == ch:
            return False
    return True

print("Sudoku validity check demo:", is_valid(
    [["."]*9 for _ in range(9)], 0, 0, "5"))
