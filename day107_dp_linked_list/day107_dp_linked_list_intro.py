"""
Day 107: DP / Linked List
Dynamic Programming helps solve problems with optimal substructure, while linked list
problems focus on pointer manipulation and incremental state updates.
"""

# Example 1: DP game strategy (minimax style)
def example_one():
    """
    DP intuition:
    dp[l][r] = minimum cost to guarantee a win in range [l, r]
    Choose k that minimizes worst-case loss.
    """
    n = 5
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            dp[l][r] = float('inf')
            for k in range(l, r):
                dp[l][r] = min(dp[l][r], k + max(dp[l][k - 1], dp[k + 1][r]))

    return dp[1][n]

print("Output Example 1:", example_one())


# Example 2: Linked list insertion
def example_two():
    """
    Demonstrates basic linked list insert at head.
    """
    class Node:
        def __init__(self, val, nxt=None):
            self.val = val
            self.next = nxt

    head = None
    for i in range(3):
        head = Node(i, head)

    # Traverse list
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    return res

print("Output Example 2:", example_two())
