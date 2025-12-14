"""
Day 105: DP / Greedy / BFS
Some problems require combining dynamic programming for optimal substructure,
greedy observations for pruning, and BFS for shortest-path or state exploration.
"""

# Example 1: DP with greedy optimization
def example_one():
    """
    Egg Drop intuition:
    DP where we choose the best floor to minimize worst-case attempts.
    Greedy observation: optimal drop floor shifts upward as moves increase.
    """
    eggs = 2
    floors = 6

    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    for e in range(1, eggs + 1):
        for f in range(1, floors + 1):
            dp[e][f] = f  # worst case

    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            for k in range(1, f + 1):
                dp[e][f] = min(
                    dp[e][f],
                    1 + max(dp[e - 1][k - 1], dp[e][f - k])
                )

    return dp[eggs][floors]

print("Output Example 1:", example_one())


# Example 2: BFS on state space
def example_two():
    """
    BFS traversal over configurations.
    Each state expands into next possible states.
    """
    from collections import deque

    start = "123450"
    target = "123045"

    q = deque([(start, 0)])
    visited = {start}

    while q:
        state, steps = q.popleft()
        if state == target:
            return steps

        idx = state.index('0')
        for nxt in [idx - 1, idx + 1]:
            if 0 <= nxt < len(state):
                arr = list(state)
                arr[idx], arr[nxt] = arr[nxt], arr[idx]
                new_state = "".join(arr)

                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, steps + 1))

    return -1

print("Output Example 2:", example_two())
