"""
Day 17: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Generate Parentheses (LeetCode 22, Medium)
# Link: https://leetcode.com/problems/generate-parentheses/
# ---------------------------------------------------------
class SolutionGenerateParentheses:
    def generateParenthesis(self, n: int) -> list[str]:
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


# ---------------------------------------------------------
# Problem 2: Word Search (LeetCode 79, Medium)
# Link: https://leetcode.com/problems/word-search/
# ---------------------------------------------------------
class SolutionWordSearch:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[idx]:
                return False

            tmp, board[r][c] = board[r][c], "#"
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


# ---------------------------------------------------------
# Problem 3: Palindrome Partitioning (LeetCode 131, Medium)
# Link: https://leetcode.com/problems/palindrome-partitioning/
# ---------------------------------------------------------
class SolutionPalindromePartitioning:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                if s[start:end] == s[start:end][::-1]:  # palindrome check
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Generate Parentheses:", SolutionGenerateParentheses().generateParenthesis(3))
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    print("Word Search:", SolutionWordSearch().exist(board, "SEE"))
    print("Palindrome Partitioning:", SolutionPalindromePartitioning().partition("aab"))
