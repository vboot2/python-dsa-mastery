"""
Day 81: DP Sequence/Path
Sequence DP handles structured recurrence formulas.
Path DP solves grid or movement-based problems with state transitions.
"""

# ---------------------------------------------------------
# Example 1: Catalan DP (Unique BST Count - LC 96 concept)
# ---------------------------------------------------------

def example_one(n):
    """
    Classic Catalan number DP.
    dp[i] = number of unique BSTs using i nodes.
    """
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            left = dp[root - 1]
            right = dp[nodes - root]
            total += left * right
        dp[nodes] = total

    return dp[n]

print("Output Example 1:", example_one(3))


# ---------------------------------------------------------
# Example 2: Path Counting with Boundaries (LC 576 idea)
# ---------------------------------------------------------

def example_two(m, n, maxMoves, startRow, startCol):
    """
    Counts paths moving out of grid boundary within maxMoves.
    DP[row][col] = number of ways from (row, col) with remaining moves.
    """
    MOD = 10**9 + 7
    dp = [[0] * n for _ in range(m)]
    dp[startRow][startCol] = 1
    result = 0

    for _ in range(maxMoves):
        next_dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                # If moving out of boundary:
                ways = dp[r][c]
                if r == 0: result += ways
                if r == m-1: result += ways
                if c == 0: result += ways
                if c == n-1: result += ways

                # Move inside grid
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < m and 0 <= cc < n:
                        next_dp[rr][cc] = (next_dp[rr][cc] + ways) % MOD
        dp = next_dp

    return result % MOD

print("Output Example 2:", example_two(2, 2, 2, 0, 0))
