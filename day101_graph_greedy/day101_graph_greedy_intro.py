"""
Day 101: Graph / Greedy
Greedy and graph algorithms often intersect in optimization problems like
finding minimal swaps, constructing paths, or scheduling under constraints.
"""

# ---------------------------------------------------------
# Example 1: Graph Matching (Greedy Swapping Logic)
# ---------------------------------------------------------
def example_one():
    """
    Minimum swaps to pair couples (LC 765).
    Use union-find or mapping to track misplaced pairs.
    """
    row = [0, 2, 1, 3]
    n = len(row) // 2
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        parent[find(a)] = find(b)

    for i in range(0, len(row), 2):
        a, b = row[i] // 2, row[i + 1] // 2
        union(a, b)

    components = len({find(i) for i in range(n)})
    return n - components  # swaps needed

print("Output Example 1:", example_one())


# ---------------------------------------------------------
# Example 2: Eulerian Path Construction (LC 753 inspiration)
# ---------------------------------------------------------
def example_two():
    """
    Build de Bruijn sequence using DFS – minimal combination coverage.
    """
    n, k = 2, 2
    seen = set()
    res = []

    def dfs(node):
        for x in map(str, range(k)):
            edge = node + x
            if edge not in seen:
                seen.add(edge)
                dfs(edge[1:])
                res.append(x)

    dfs("0" * (n - 1))
    return "".join(res) + "0" * (n - 1)

print("Output Example 2:", example_two())
