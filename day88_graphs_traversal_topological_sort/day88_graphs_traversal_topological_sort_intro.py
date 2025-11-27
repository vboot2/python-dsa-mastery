""" Day 88: Graphs – Traversal / Topological Sort
Understanding DFS/BFS traversal and ordering nodes in a DAG using topological sorting.
"""

# Example 1: Simple Topological Sort (Kahn's Algorithm)
def example_one():
    from collections import deque

    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    indegree = {i: 0 for i in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([node for node in indegree if indegree[node] == 0])
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return f"Topological Order: {topo}"


print("Output Example 1:", example_one())


# Example 2: DFS-based Topological Sort
def example_two():
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [1]
    }

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return f"Topological Order (DFS): {stack[::-1]}"


print("Output Example 2:", example_two())
