"""
Day 106: DP / Graph
Problems in this category combine dynamic programming for optimal substructure
with graph traversal or graph-based state transitions.
"""

# Example 1: DP on strings (palindrome partition intuition)
def example_one():
    """
    DP idea:
    - Precompute palindrome substrings
    - DP[i] = minimum cuts/parts for prefix ending at i
    """
    s = "aab"
    n = len(s)

    # palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True

    dp = [float('inf')] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 1
        else:
            for j in range(i):
                if is_pal[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

print("Output Example 1:", example_one())


# Example 2: Graph shortest path with 0-1 BFS
def example_two():
    """
    Graph with edge weights 0 or 1.
    Use deque for efficient shortest path computation.
    """
    from collections import deque

    grid = [
        [1, 1, 3],
        [3, 2, 2],
        [1, 1, 4]
    ]
    m, n = len(grid), len(grid[0])

    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    dq = deque([(0, 0)])
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0

    while dq:
        r, c = dq.popleft()
        for i, (dr, dc) in enumerate(dirs, 1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = 0 if grid[r][c] == i else 1
                if dist[r][c] + cost < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + cost
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    return dist[m - 1][n - 1]

print("Output Example 2:", example_two())
