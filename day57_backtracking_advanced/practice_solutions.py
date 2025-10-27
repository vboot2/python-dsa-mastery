"""
Day 57: Backtracking (Advanced) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: N-Queens II (LeetCode 52, Hard)
# Link: https://leetcode.com/problems/n-queens-ii/
# ---------------------------------------------------------


class SolutionProblemOne:
    def solve(self, n):
        """
        Count total number of distinct N-Queens solutions.
        """
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        count = 0

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                backtrack(r + 1)
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return count


# ---------------------------------------------------------
# Problem 2: Word Search II (LeetCode 212, Hard)
# Link: https://leetcode.com/problems/word-search-ii/
# ---------------------------------------------------------


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class SolutionProblemTwo:
    def solve(self, board, words):
        """
        Find all words from the list that exist in the board.
        Uses Trie + Backtracking (DFS).
        """
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            curr = node.children.get(ch)
            if not curr:
                return

            if curr.word:
                res.append(curr.word)
                curr.word = None  # avoid duplicates

            board[r][c] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr.children:
                    dfs(nr, nc, curr)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return res


# ---------------------------------------------------------
# Example runs
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Problem 1 Example (N-Queens II):", SolutionProblemOne().solve(4))

    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(
        "Problem 2 Example (Word Search II):", SolutionProblemTwo().solve(board, words)
    )
