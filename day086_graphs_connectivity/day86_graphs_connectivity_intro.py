""" Day 86: Graphs Connectivity
Understanding how to determine if nodes in a graph are connected using BFS, DFS, or Union-Find.
"""

# Example 1: Using BFS to check if target is reachable from source
def example_one():
    # Graph represented as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    # BFS to check connectivity
    from collections import deque
    q = deque([0])
    visited = set([0])

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return "Is 3 reachable from 0? -> " + str(3 in visited)


print("Output Example 1:", example_one())


# Example 2: Union-Find based connectivity
def example_two():
    parent = {i: i for i in range(4)}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pb] = pa

    # Connect nodes
    union(0, 1)
    union(1, 3)
    # Component: 0-1-3, isolated: 2

    return "Are 0 and 3 connected? -> " + str(find(0) == find(3))


print("Output Example 2:", example_two())
