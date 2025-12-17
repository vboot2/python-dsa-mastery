"""
Day 17: Recursion, Sorting, Searching

These problems continue exploring recursion + backtracking:
- Generating valid strings with constraints
- Exploring a grid using DFS/backtracking
- Partitioning strings based on conditions (palindromes)
"""

# -------------------------------
# Example 1: Generate parentheses (mini demo)
# -------------------------------
def generate_parentheses(n: int) -> list[str]:
    res = []

    def backtrack(open_count, close_count, path):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count, path)
            path.pop()
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return res

print("Parentheses n=3:", generate_parentheses(3))


# -------------------------------
# Example 2: Word search on a board
# -------------------------------
def word_exists(board, word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:
            return False

        tmp, board[r][c] = board[r][c], "#"  # mark visited
        found = (backtrack(r+1, c, idx+1) or
                 backtrack(r-1, c, idx+1) or
                 backtrack(r, c+1, idx+1) or
                 backtrack(r, c-1, idx+1))
        board[r][c] = tmp
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
print("Word 'ABCCED' exists:", word_exists(board, "ABCCED"))


# -------------------------------
# Example 3: Palindrome check + partitioning demo
# -------------------------------
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print("Palindrome check for 'racecar':", is_palindrome("racecar"))
