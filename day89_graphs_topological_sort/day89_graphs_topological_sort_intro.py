""" Day 89: Graphs - Topological Sort
Topological sorting orders nodes of a DAG so all directed edges go from left to right.
"""

# Example 1: Kahn's Algorithm (BFS-based Topological Sort)
def example_one():
    from collections import deque

    graph = {
        0: [2, 3],
        1: [3],
        2: [4],
        3: [4],
        4: []
    }

    indegree = {i: 0 for i in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([x for x in graph if indegree[x] == 0])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return f"Kahn's Topological Order: {order}"


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

    return f"DFS Topological Order: {stack[::-1]}"


print("Output Example 2:", example_two())
