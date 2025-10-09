""" 
Day 39: Graphs, Union-Find, Tries 
Topological Sorting, Course Scheduling, and Safe Nodes
"""

# Example 1: Topological Sort (Kahn’s Algorithm)
def example_one():
    """
    Perform topological sorting using Kahn's algorithm.
    """
    from collections import deque

    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: []
    }

    indegree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    q = deque([u for u in indegree if indegree[u] == 0])
    topo = []

    while q:
        node = q.popleft()
        topo.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return topo  # Expected: [0, 1, 2, 3]


# Example 2: Detecting Cycles in a Directed Graph (DFS)
def example_two():
    """
    Use DFS to detect cycles in a directed graph.
    """
    graph = {
        0: [1],
        1: [2],
        2: [0],  # cycle
        3: [4],
        4: []
    }

    visited = [0] * len(graph)  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        if visited[node] == 1:
            return True  # found cycle
        if visited[node] == 2:
            return False
        visited[node] = 1
        for nei in graph[node]:
            if dfs(nei):
                return True
        visited[node] = 2
        return False

    for node in graph:
        if dfs(node):
            return True  # cycle exists
    return False  # no cycle


if __name__ == "__main__":
    print("Output Example 1 (Topological Sort):", example_one())
    print("Output Example 2 (Cycle Detection):", example_two())
