"""
Day 16: Recursion, Sorting, Searching

Continuation of recursion with backtracking.
- Backtracking systematically explores all possibilities
- Sorting often helps avoid duplicates
- Search strategies are embedded in recursion/DFS
"""

# -------------------------------
# Example 1: Recursive Fibonacci
# -------------------------------
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(6):", fibonacci(6))


# -------------------------------
# Example 2: Generating all subsets
# -------------------------------
def generate_subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

print("Subsets of [1,2,3]:", generate_subsets([1, 2, 3]))


# -------------------------------
# Example 3: N-Queens board setup (recursive placement idea)
# -------------------------------
def solve_n_queens(n: int):
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r, cols, diag1, diag2):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            board[r][c] = "Q"
            backtrack(r+1, cols | {c}, diag1 | {r-c}, diag2 | {r+c})
            board[r][c] = "."

    backtrack(0, set(), set(), set())
    return res

print("N-Queens for n=4:", solve_n_queens(4))
